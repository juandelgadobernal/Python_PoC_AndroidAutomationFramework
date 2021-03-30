"""Test functions Module"""
from  lib.adb.adbcontroller import AdbController
from lib.mydevice.mydevice import MyDevice

class TestFunctions():
    """TestFunctions class"""

    def __init__(self, my_device: MyDevice):
        self.my_device = my_device

    def test_make_phone_call(self, phone_number):
        """
        Function to make a phone call using the AdbController class
        param str phone_number: the phone number to call
        returns: a boolean true if the call is made succesfully, false otherwise
        """
        controller = AdbController(self.my_device.device_id)
        result = controller.make_phone_call_adb(phone_number)
        return result

    def test_download_logcat(self, log_name):
        """
        Function to download the logcat of a phone in the PC
        param str log_name: Name of the file where the logcat will be saved
        returns: a boolean true if the the logcat was succesfully saved, false otherwise
        """
        try:
            self.my_device.download_log(log_name)
            log_file = self.my_device.open_log(log_name)
            content = log_file.read()
        finally:
            self.my_device.close_log(log_file)
        return  len(content) > 0

    def test_open_app(self, package_name):
        """
        Function to open an application in the phone
        param str package_name: the package name of the app to be opened
        returns: a boolean true if the app was succesfully opened, false otherwise
        """
        result = self.my_device.open_app(package_name)
        return result

    def test_close_app(self, package_name):
        """
        Function to close an application in the phone
        param str package_name: the package name of the app to be closed
        returns: a boolean true if the app was succesfully closed, false otherwise
        """
        return self.my_device.close_app(package_name)

    def test_download_apk(self, apk_url):
        """
        Function to download an apk from an URL
        param str apk_url: the URL where the apk is
        returns: a boolean true if the app was succesfully installed, false otherwise
        """
        apk_path = self.my_device.download_apk(apk_url)
        return apk_path

    def test_install_apk(self, apk_path):
        """
        Function to install an application from an apk saved in the PC
        param str apk_path: the location and name in the PC of the apk to be installed in the phone
        returns: a boolean true if the app was succesfully isntalled, false otherwise
        """
        parts = apk_path.split("/")
        apk_name = parts[len(parts) - 1]
        message = "{} couldn't be installed".format(apk_name)
        return self.my_device.upload_install_app(apk_name), message

    def test_end_call(self):
        """
        Function to finish a phone call that was previously started
        returns: a boolean true if the call was succesfully finished, false otherwise
        """
        return self.my_device.end_call()

    def test_timer(self, time):
        """
        Function to pause the execution of the script for a certain time
        param int time: time in milliseconds that the script will be paused
        returns:
        """
        self.my_device.sleep_call(time)

    def test_validate_phone_number(self, file_name, phone_number):
        """
        Function that validates if a phone number was registered in a log file
        param str file_name: the name of the log file where the phone number will be searched
        param str phone_number: phone number to be searched
        returns: a boolean true if the phone number was found in the file, false otherwise
        """
        return self.my_device.find_in_log(file_name, phone_number)
