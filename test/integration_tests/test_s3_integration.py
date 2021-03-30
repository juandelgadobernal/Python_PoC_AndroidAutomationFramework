"""Test S3 Integration Module"""
# pylint: disable=E1101
import time
import pytest
from lib.myapp.facebook import Facebook
from lib.logs.logger import Logger
from lib.filemanager.filemanager import FileManager

@pytest.mark.integration_tests
class TestS3Integration():
    """Test S3 Integration Class"""
    def test_facebook_login(self):
        """
        Logs in a Facebook account with the given username and pasword
        Pre-requisites: the user must be in the
        """
        facebook = Facebook(self.phone_id)
        assert facebook.login(self.email, self.password)

    def test_bluetooth(self):
        """
        Verifies that the functions to turn on and off the bluetooth work properly
        Pre-requisites: Bluetooth must be turned off at the beginning of the run
        of the test.
        """
        assert self.my_device.toggle_bluetooth(True)
        time.sleep(5)
        assert self.my_device.toggle_bluetooth(False)

    @staticmethod
    def test_logger():
        """
        Verifies that the logger class saves properly the log
        messages in a file.
        Pre-requisites: None
        """
        Logger.debug("test debug")
        Logger.info("test info")
        Logger.success("test success")
        Logger.warning("test warning")
        Logger.info("test info")
        file_name = Logger.log_file.file_obj.name
        Logger.log_file = None
        log_file = FileManager(file_name, "r")
        content = log_file.read()
        assert not content

    def test_wifi(self):
        """
        Verifies that the Wi-fi is correctly turned on and off.
        Pre-requisites: Wi-fi must be turned on at the beggining of the run
        of the test.
        """
        self.my_device.turn_wifi(False)
        wifi_status = self.my_device.adb_controller.run_command(["shell", "dumpsys", "wifi"])
        indx = wifi_status.index("Wi-Fi is")
        wifi_status = wifi_status[indx+len("Wi-Fi is ") : indx+len("Wi-Fi is disabled")]
        assert wifi_status == "disabled"
        time.sleep(5)
        self.my_device.turn_wifi(True)
        wifi_status = self.my_device.adb_controller.run_command(["shell", "dumpsys", "wifi"])
        indx = wifi_status.index("Wi-Fi is")
        wifi_status = wifi_status[indx+len("Wi-Fi is ") : indx+len("Wi-Fi is enabled")]
        assert wifi_status == "enabled"
