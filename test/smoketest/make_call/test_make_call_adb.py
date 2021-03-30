"""Test make call adb Module"""
# pylint: disable=E1101,R0903
import pytest
from lib.adb.adbcontroller import AdbController

@pytest.mark.smoketest
class TestMakeCallAdb():
    """Test make call with ADB"""

    def test_make_call_adb(self):
        """
        Function to test the method to call using adb command
        Pre-conditions: the cellphone need to be unlock
        """
        controller = AdbController(self.phone_id)
        result = controller.make_phone_call_adb(self.phone_number)
        assert result
