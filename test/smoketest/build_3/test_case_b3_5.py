"""TestCase5Build3 Module"""
# pylint: disable=E1101,R0903
import os
import pytest

FACEBOOK_PACKAGE = "com.facebook.katana"
INSTAGRAM_PACKAGE = "com.instagram.android"
YOUTUBE_PACKAGE = "com.google.android.youtube"

@pytest.mark.test_cases
class TestCase5Build3():
    """TestCase5Build3 class"""
    def test_case_5(self):
        """
        Verifies Facebook, Instagram and Youtube are succesfully opened
        in the phone. Then verifies that five consecutive phone calls are
        successfully started and finished
        Pre-requisites: Facebook, Instagram and Youtube must be installed.
        The phone number must consist of 10 numeric digits and corresponds
        to a existing phone number
        """
        test_route = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'test_case_b3_2.py'))
        result_code_2 = pytest.main(["-s", test_route])

        test_route = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'test_case_b3_4.py'))
        result_code_4 = pytest.main(["-s", test_route])

        self.test_functions.test_timer(1000)
        assert result_code_2 == 0 and result_code_4 == 0
