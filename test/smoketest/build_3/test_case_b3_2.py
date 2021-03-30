"""TestCase2Build3 Module"""
# pylint: disable=E1101,R0903
import pytest
from lib.logs.logger import Logger

FACEBOOK_PACKAGE = "com.facebook.katana"
YOUTUBE_PACKAGE = "com.google.android.youtube"
INSTAGRAM_PACKAGE = "com.instagram.android"

@pytest.mark.test_cases
class TestCase2Build3():
    """TestCase2Build3 class"""
    def test_case_2(self):
        """
        Verifies Facebook, Instagram and Youtube are succesfully opened
        in the phone
        Pre-requisites: Facebook, Instagram and Youtube must be installed
        """
        package_names = [FACEBOOK_PACKAGE, INSTAGRAM_PACKAGE, YOUTUBE_PACKAGE]
        for app in package_names:
            assert self.test_functions.test_open_app(app)
            Logger.success("Se abrió la aplicación " + app)
            self.test_functions.test_timer(2000)
