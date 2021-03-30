"""TestStf Module"""
# pylint: disable=E1101
import subprocess
import re
from urllib.parse import urljoin
import requests
from lib.stfdevice.stfdevice import StfDevice

class TestStf():
    """TestStf Class"""
    def is_reserved(self):
        """
        Verifies that the device is under control of the current user. Throws
        an exception if the state of the device could not be verified.
        Pre-condition: Running OpenSTF instance with both Auth keys and ADB
        keys added correctly
        returns: boolean value indicating if device is being used
        """
        headers = {
            "Content-type": "application/json",
            "Authorization": "Bearer " + self.token
        }
        url = urljoin(self.stf_url, "/api/v1/user/devices")
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        json = res.json()
        if not json["success"]:
            raise ConnectionRefusedError(json["description"])
        reserved = False
        for device in json["devices"]:
            if device["serial"] == self.phone_id:
                reserved = True
                break
        return reserved

    @staticmethod
    def is_connected(remote_address):
        '''
        Verifies that the device is accessible from ADB.
        param str remote_address: the remote id of the device
        Pre-condition: Running OpenSTF instance with both Auth keys and ADB
        keys added correctly
        returns: boolean value indicating if device is accessible from ADB.
        '''
        command = ["adb", "devices"]
        c_one = subprocess.Popen(command, stdout=subprocess.PIPE)
        output = str(c_one.communicate()[0])
        output = re.sub(r"^b", "", output)
        output = re.sub(r"^\'|\'$", "", output)
        tofind = "{id}\\tdevice".format(id=remote_address)
        return output.find(tofind) != -1

    def test_stf_device_init(self):
        '''
        Validates that the device is ready to use after initializing. This means
        the device is both reserved and accessible from ADB.
        Pre-condition: Running OpenSTF instance with both Auth keys and ADB
        keys added correctly
        '''
        device = StfDevice(self.stf_url, self.token, self.phone_id)
        remote_address = device.get_connection_address()

        assert self.is_reserved() and self.is_connected(remote_address)

    def test_stf_device_disconnect(self):
        '''
        Validates that the device is not accessible from ADB after disconnecting.
        Pre-condition: Running OpenSTF instance with both Auth keys and ADB
        keys added correctly
        '''
        stfdevice = StfDevice(self.stf_url, self.token, self.phone_id)
        remote_address = stfdevice.get_connection_address()
        stfdevice.disconnect_device()

        assert not self.is_connected(remote_address)

    def test_stf_device_remove(self):
        '''
        Validates that the device is not reserved after removing the device.
        Pre-condition: Running OpenSTF instance with both Auth keys and ADB
        keys added correctly
        '''
        stfdevice = StfDevice(self.stf_url, self.token, self.phone_id)
        stfdevice.disconnect_device()
        stfdevice.remove_device()
        assert not self.is_reserved()
