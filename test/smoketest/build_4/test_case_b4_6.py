"""TestCase6Build4 Module"""
# pylint: disable=E1101,R0903
import pytest

INSTAGRAM_PACKAGE = "com.instagram.android"
FACEBOOK_PACKAGE = "com.facebook.katana"
YOUTUBE_PACKAGE = "com.google.android.youtube"

@pytest.mark.test_cases
class TestCase6Build4():
    """TestCase6Build4 class"""
    def test_case_6(self):
        """
        Verifies Facebook, Instagram and Youtube are succesfully opened
        in the phone. Then verifies that five consecutive phone calls are
        successfully started and finished
        Pre-requisites: Facebook, Instagram and Youtube must be installed.
        The phone number must consist of 10 numeric digits and corresponds
        to a existing phone number
        """
        self.test_case_b4_2.test_case_2()
        self.test_case_b4_5.test_case_5()
