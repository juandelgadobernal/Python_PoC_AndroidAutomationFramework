"""Test S2 Integration Module"""
# pylint: disable=E1101
import os
import time
import pytest
from lib.filemanager.filemanager import FileManager

SPOTIFY_PACKAGE = "com.spotify.music"
INSTAGRAM_PACKAGE = "com.instagram.android"
TWITTER_PACKAGE = "com.twitter.android"

@pytest.mark.integration_tests
class TestS2Integration():
    """Test S2 Integration Class"""
    def test_file_manager(self):
        """
        Validates that a folder is created, that a file can be read
        if the needed permissions are given and that it also can be
        written.
        Pre-condition: a file with the given name must exist
        """
        FileManager.directory_exists_create(self.directory_name)
        try:
            file = open(self.file_name, "r")
            file.close()
        except IOError:
            file = open(self.file_name, "w")
            file.write("initial content")
            file.close()
        try:
            message = "Couln't create directory: {}".format(self.directory_name)
            assert os.path.exists(self.directory_name), message
            file_size = os.path.getsize(self.file_name)
            file_manager = FileManager(self.file_name, "r")
            content = file_manager.read()
            not_match = "File sizes doesn't match, expected:"
            message = "{} {}, found: {}".format(not_match, file_size, len(content))
            assert len(content) == file_size, message
            file_manager = FileManager(self.file_name, "w")
            file_manager.write(self.write_string)
            new_size = os.path.getsize(self.file_name)
            message = "{} {}, found: {}".format(not_match, new_size, len(self.write_string))
            assert new_size == len(self.write_string), message
        finally:
            os.remove(self.file_name)

    def test_install_apk(self):
        """
        Validates that an apk is correctly downloaded, saved and installed
        in a device.
        Pre-condition: The computer must be connected to the internet, the
        url must direct to a valid apk
        """
        apk_path = self.my_device.download_apk(self.apk_url)
        assert os.path.exists(apk_path), "couldn't download from {}".format(self.apk_url)
        parts = apk_path.split("/")
        apk_name = parts[len(parts) - 1]
        message = "{} couldn't be installed".format(apk_name)
        assert self.my_device.upload_install_app(apk_name), message
        command = "adb -s {} shell pm list packages".format(self.my_device.device_id)
        result = os.popen(command).read()
        message = "{} wasn't installed in the phone".format(self.package_name)
        assert "package:{}".format(self.package_name) in result, message

    def test_open_and_close_apps(self):
        """
        Validates that the back and home buttons work properly, opening many apps and then
        pressing these buttons
        pre-conditions: The applications must be installed in the device.
        """
        package_names = [SPOTIFY_PACKAGE, INSTAGRAM_PACKAGE, TWITTER_PACKAGE]
        for app in package_names:
            self.my_device.open_app(app)
            time.sleep(3)
        self.my_device.back_button()
        time.sleep(3)
        self.my_device.go_home()

    def test_close_all(self):
        """
        Validates that, when many applications are oppen simultaniously, they can all close
        at the same time
        pre-conditions: The applications must be installed in the device.
        The method has been thought for Motorola, Samsung, Huawei and LG devices
        """
        package_names = [SPOTIFY_PACKAGE, INSTAGRAM_PACKAGE, TWITTER_PACKAGE]
        for app in package_names:
            self.my_device.open_app(app)
            time.sleep(3)
        assert self.my_device.clear_apps(), "The applications didn't close succesfully"
                