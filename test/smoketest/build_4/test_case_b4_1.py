"""TestCase1Build4 Module"""
# pylint: disable=E1101,R0903
import pytest
from lib.logs.logger import Logger

@pytest.mark.test_cases
class TestCase1Build4():
    """TestCase1Build4 class"""
    def test_case_1(self):
        """
        Verifies that a phone call is succesuflly started and finished
        Pre-requisites: The phone number must consist of 10 numeric
        digits and corresponds to a existing phone number
        """
        assert self.test_functions.test_make_phone_call(self.phone_number)
        Logger.success("Se inicio una llamada")
        self.test_functions.test_timer(9000)
        assert self.test_functions.test_end_call()
        Logger.success("Se terminó una llamada")
        self.test_functions.test_timer(9000)
