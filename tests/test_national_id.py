from unittest import TestCase

from loguru import logger

from ..utils.national_id import NationalID


class NationalIDValidatorTests(TestCase):
    def setUp(self):
        logger.info(f"Test case : {self._testMethodName}")

    def tearDown(self):
        pass

    def test01_valid_national_id_number(self):
        """Test case for valid national id number with correct data.

        **Test Scenario**
        - Get the class instance.
        - Get the national id number and make sure they are equal
        """
        number = "29509181201214"
        instance = NationalID(number)
        validity, data = instance.get_info()
        self.assertTrue(validity)
        self.assertEqual(
            data,
            {
                "year_of_birth": "1995",
                "month_of_birth": "9",
                "day_of_birth": "18",
                "governorate": "Al Daqhlia",
                "type": "Male",
            },
        )

    def test02_invalid_national_id_number_century(self):
        """Test case for valid national id number with invalid data.

        **Test Scenario**
        - Get the class instance.
        - Get the national id number with wrong century and make sure they are not equal
        """
        number = "49509181201214"
        instance = NationalID(number)
        validity, error = instance.get_info()
        self.assertFalse(validity)
        self.assertEqual(
            error, {"Error": f"Invalid national ID number: {number}. Please enter the correct one"},
        )

    def test03_invalid_national_id_number_year(self):
        """Test case for valid national id number with invalid data.

        **Test Scenario**
        - Get the class instance.
        - Get the national id number with wrong year and make sure they are not equal
        """
        number = "39509181201214"  # year 2095 is not there yet
        instance = NationalID(number)
        validity, error = instance.get_info()
        self.assertFalse(validity)
        self.assertEqual(
            error, {"Error": f"Invalid national ID number: {number}. Please enter the correct one"},
        )

    def test04_invalid_national_id_number_month(self):
        """Test case for valid national id number with invalid data.

        **Test Scenario**
        - Get the class instance.
        - Get the national id number with wrong month and make sure they are not equal
        """
        number = "29513181201214"
        instance = NationalID(number)
        validity, error = instance.get_info()
        self.assertFalse(validity)
        self.assertEqual(
            error, {"Error": f"Invalid national ID number: {number}. Please enter the correct one"},
        )

    def test05_invalid_national_id_number_day(self):
        """Test case for valid national id number with invalid data.

        **Test Scenario**
        - Get the class instance.
        - Get the national id number with wrong day and make sure they are not equal
        """
        number = "29510351201214"
        instance = NationalID(number)
        validity, error = instance.get_info()
        self.assertFalse(validity)
        self.assertEqual(
            error, {"Error": f"Invalid national ID number: {number}. Please enter the correct one"},
        )

    def test06_invalid_national_id_number_day_febuary(self):
        """Test case for valid national id number with invalid data.

        **Test Scenario**
        - Get the class instance.
        - Get the national id number with wrong day (feb has 28 or 29 day) and make sure they are not equal
        """
        number = "29502301201214"
        instance = NationalID(number)
        validity, error = instance.get_info()
        self.assertFalse(validity)
        self.assertEqual(
            error, {"Error": f"Invalid national ID number: {number}. Please enter the correct one"},
        )

    def test07_invalid_national_id_number_day_febuary_29(self):
        """Test case for valid national id number with invalid data.

        **Test Scenario**
        - Get the class instance.
        - Get the national id number with wrong day (feb has 28 or 29 day) and make sure they are not equal
        """
        number = "29502291201214"
        instance = NationalID(number)
        validity, error = instance.get_info()
        self.assertFalse(validity)
        self.assertEqual(
            error, {"Error": f"Invalid national ID number: {number}. Please enter the correct one"},
        )

    def test08_invalid_national_id_number_day_30_months(self):
        """Test case for valid national id number with invalid data.

        **Test Scenario**
        - Get the class instance.
        - Get the national id number with wrong day (30 days month) and make sure they are not equal
        """
        number = "29509311201214"
        instance = NationalID(number)
        validity, error = instance.get_info()
        self.assertFalse(validity)
        self.assertEqual(
            error, {"Error": f"Invalid national ID number: {number}. Please enter the correct one"},
        )

    def test09_invalid_national_id_number_governate_code(self):
        """Test case for valid national id number with invalid data.

        **Test Scenario**
        - Get the class instance.
        - Get the national id number with invalid gouvernate code and make sure they are not equal
        """
        number = "29509227001214"
        instance = NationalID(number)
        validity, error = instance.get_info()
        self.assertFalse(validity)
        self.assertEqual(
            error, {"Error": f"Invalid national ID number: {number}. Please enter the correct one"},
        )
