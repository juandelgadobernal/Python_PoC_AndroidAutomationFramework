"""TestCase2Build4 Module"""
# pylint: disable=E1101,R0903
import pytest
from lib.logs.logger import Logger

YOUTUBE_PACKAGE = "com.google.android.youtube"
FACEBOOK_PACKAGE = "com.facebook.katana"
INSTAGRAM_PACKAGE = "com.instagram.android"


@pytest.mark.test_cases
class TestCase2Build4():
    """TestCase2Build4 class"""
    def test_case_2(self):
        """
        Verifies Facebook, Instagram and Youtube are succesfully opened
        Pre-requisites: Facebook, Instagram and Youtube must be installed on the phone
        """
        package_names = [FACEBOOK_PACKAGE, INSTAGRAM_PACKAGE, YOUTUBE_PACKAGE]
        for app in package_names:
            assert self.test_functions.test_open_app(app)
            Logger.success("Se abrió la aplicación " + app)

            self.test_functions.test_timer(2000)
