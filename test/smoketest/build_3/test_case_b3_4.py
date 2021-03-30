"""TestCase4Build3 Module"""
# pylint: disable=E1101,R0903
import pytest
from lib.logs.logger import Logger

@pytest.mark.test_cases
class TestCase4Build3():
    """TestCase4Build3 class"""
    def test_case_4(self):
        """
        Verifies that five consecutive phone calls are
        successfully started and finished
        Pre-requisites: The phone number must consist of 10 numeric
        digits and corresponds to a existing phone number
        """
        for i in range(1, 6):
            assert self.test_functions.test_make_phone_call(self.phone_number)
            Logger.success("Se inicio la llamada " + str(i))
            self.test_functions.test_timer(5000)
            assert self.test_functions.test_end_call()
            Logger.success("Se terminó la llamada " + str(i))
            self.test_functions.test_timer(5000)
