from unittest import TestCase

from loguru import logger
from server import app
from webtest import TestApp, AppError


class NationalIDValidatorTests(TestCase):
    def setUp(self):
        logger.info(f"Test case : {self._testMethodName}")
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        self.app = TestApp(app)

    def test01_endpoint_with_valid_national_id_number(self):
        """Test case for making sure endpoint is will respond as ok with the valid payload

        **Test Scenario**
        - Post the national id number
        - compare the national id number and response make sure they are equal
        """
        number = "29509181201214"
        response = self.app.post("/get_info", params=f'{{"id_number": "{number}"}}', content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertEqual(
            response.json,
            {
                "nationl_id_data": {
                    "year_of_birth": "1995",
                    "month_of_birth": "9",
                    "day_of_birth": "18",
                    "governorate": "Al Daqhlia",
                    "type": "Male",
                }
            },
        )

    def test02_endpoint_with_invalid_national_id_number(self):
        """Test case for making sure endpoint is will respond as ok with the invalid payload

        **Test Scenario**
        - Post the national id number
        - Response will be 400 bad request
        """
        number = "49509181201214"
        with self.assertRaises(AppError):
            # expect a 400 bad request
            self.app.post("/get_info", params=f'{{"id_number": "{number}"}}', content_type="application/json")
