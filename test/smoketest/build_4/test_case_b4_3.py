"""TestCase3Build4 Module"""
# pylint: disable=E1101,R0903
import pytest
from lib.logs.logger import Logger

@pytest.mark.test_cases
class TestCase3Build4():
    """TestCase3Build4 class"""
    def test_case_3(self):
        """
        Verifies an apk is successfully downloaded from an URL in
        the PC and installed in phone. Then verifies that a call is successfully made
        Pre-requisites: The URL must be a valid apk location
        """
        apk_path = self.test_functions.test_download_apk(self.apk_url)
        Logger.success("Se descargó un apk")
        assert self.test_functions.test_install_apk(apk_path)
        Logger.success("Se instaló un apk")
        self.test_case_b4_1.test_case_1()
