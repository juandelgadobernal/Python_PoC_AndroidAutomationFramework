"""Test S1 Integration Module"""
# pylint: disable=E1101
import time
import datetime
import pytest

PLAYSTORE_PACKAGE_NAME = "com.ethicalhackx.myapplication"

@pytest.mark.integration_tests
class TestSprint():
    """Test S1 Integration Class"""
    def test_install_app(self):
        """
        Validates that an an application is correclty installed from the Play Store
        in a device.
        Pre-condition: The package_name must correspond to the package name of an
        application in the Play Store, and that application must not be installed in
        the device.
        """
        try:
            self.my_device.install_app(PLAYSTORE_PACKAGE_NAME)
            assert self.my_device.open_app(PLAYSTORE_PACKAGE_NAME)
            time.sleep(5)
            self.my_device.close_app(PLAYSTORE_PACKAGE_NAME)
            command = ["shell", "pm", "list packages"]
            result = self.my_device.adb_controller.run_command(command)
            message = "{} wasn't installed in the phone".format(self.package_name)
            assert "package:{}".format(PLAYSTORE_PACKAGE_NAME) in result, message
        finally:
            command = ["uninstall", PLAYSTORE_PACKAGE_NAME]
            self.my_device.adb_controller.run_command(command)

    def test_logcat(self):
        """
        Validates that the logcat of the phone is saved in a PC.
        pre-condition: The file name must be composed only by valid characters
        It may or not have a file extension. If it has, it will be replaced with .log
        """
        log_name = "{}.{}".format(str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")), "log")
        try:
            self.my_device.download_log(log_name)
            log_file = self.my_device.open_log(log_name)
            content = log_file.read()
            assert not content
        finally:
            self.my_device.close_log(log_file)
