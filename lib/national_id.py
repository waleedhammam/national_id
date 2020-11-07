from datetime import datetime

from .egypt_codes import GOVERNORATES_CODES_MAP


class NationalID:
    """National ID class, will include the skelton of it's properties
    and verification.
    """

    def __init__(self, id_number: str) -> None:
        """
        Args:
            id_number (int): Egyptian national id number
        """
        self.id_number = id_number

    def _validate(self) -> bool:
        """Validates the id number parts

        Returns:
            bool: True if it is a valid egyptian id number, False if not
        """
        if not all([self.id_number.isdigit(), len(self.id_number) == 14]):
            return False

        self.century = int(self.id_number[0])
        self.year = int(self.id_number[1:3])
        self.month = int(self.id_number[3:5])
        self.day = int(self.id_number[5:7])
        self.governorate = int(self.id_number[7:9])
        self.unique_num = int(self.id_number[9:13])
        self.verification_digit = int(self.id_number[13])

        current_datetime = datetime.now()

        century_check = self.century in [2, 3]  # we will deal with 1900 ~ 2099
        year_check = (
            (self.year <= current_datetime.year - 2000) if self.century == 3 else True
        )  # can't be in the future
        month_check = self.month in range(1, 13)

        # check for months that have 31 day and febuary which is 28 or 29
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            day_check = self.day in range(1, 32)
        elif self.month in [4, 6, 9, 11]:
            day_check = self.day in range(1, 31)
        elif self.month == 2:
            day_check = self.day in range(30) if self.year % 4 == 0 else self.day in range(29)
        else:
            day_check = False

        governorate_check = self.governorate in GOVERNORATES_CODES_MAP

        return all([century_check, year_check, month_check, day_check, governorate_check])

    def get_info(self) -> tuple:
        """Process the data from the id number into readable format

        Returns:
            tuple(bool, str): True if valid_id else False, json string for the collective information that will return to user
        """
        id_owner_data = {}
        if not self._validate():
            number_error_msg = f"Invalid national ID number: {self.id_number}. Please enter the correct one"
            return False, {"error": number_error_msg}

        id_owner_data["year_of_birth"] = f"20{self.year}" if self.century == 3 else f"19{self.year}"
        id_owner_data["month_of_birth"] = f"{self.month}"
        id_owner_data["day_of_birth"] = f"{self.day}"
        id_owner_data["governorate"] = GOVERNORATES_CODES_MAP[self.governorate]
        id_owner_data["type"] = "Male" if self.unique_num % 2 != 0 else "Female"

        return True, id_owner_data
