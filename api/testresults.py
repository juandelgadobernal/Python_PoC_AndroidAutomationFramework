"""TestResults Module"""
# pylint: disable=R0903
from lib.logs.logger import Logger

class TestResults:
    """TestResults Class"""
    @staticmethod
    def log_test_results(code):
        """
        Sends a message to the Logger Class
        """
        if code == 0:
            Logger.success("Prueba Exitosa")
        elif code == 1:
            Logger.warning("Prueba Fallida")
        elif code == 2:
            Logger.warning("Ejecución interrumpida por el usuario")
        else:
            Logger.error("Error interno al ejecutar la prueba")
