"""TestCase4Build4 Module"""
# pylint: disable=E1101,R0903
from datetime import datetime
import pytest
from lib.logs.logger import Logger

@pytest.mark.test_cases
class TestCase4Build4():
    """TestCase4Build4 class"""
    def test_case_4(self):
        """
        Verifies that a phone call is successully started and finished. Then, verifies that
        the phone number that received the call is the the logcat of the phone that made
        the call
        Pre-requisites: The phone number must consist of 10 numeric
        digits and corresponds to a existing phone number
        """
        self.test_case_b4_1.test_case_1()
        log_name = "{}.{}".format(str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")), "log")
        assert self.test_functions.test_download_logcat(log_name)
        Logger.success("Se descargó el logcat")
        assert self.test_functions.test_validate_phone_number(log_name, self.phone_number)
        Logger.success("Se validó el teléfono en el logcat")
