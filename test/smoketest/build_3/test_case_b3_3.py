"""TestCase3Build3 Module"""
# pylint: disable=E1101,R0903
import os
import pytest
from lib.logs.logger import Logger

@pytest.mark.test_cases
class TestCase3Build3():
    """TestCase3Build3 class"""
    def test_case_3(self):
        """
        Verifies that an apk is successfully downloaded from an URL in
        the PC and installed in a phone. Then verifies that a call is
        successfully made
        Pre-requisites: The URL must correspond to an apk location
        """
        apk_path = self.test_functions.test_download_apk(self.apk_url)
        self.test_functions.test_timer(3000)
        Logger.success("Se descargó un apk")
        assert self.test_functions.test_install_apk(apk_path)
        self.test_functions.test_timer(3000)
        Logger.success("Se instaló un apk")
        Logger.info("Ejecutando Caso de Prueba 1")
        test_route = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_case_b3_1.py'))
        pytest.main(["-s", test_route])
