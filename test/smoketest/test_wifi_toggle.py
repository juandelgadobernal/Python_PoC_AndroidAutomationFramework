"""Test toggle Wi-Fi Module"""
# pylint: disable=E1101,R0903
import pytest

@pytest.mark.test_wifi
class TestWifi():
    """Test toggle Wi-Fi"""

    def test_wifi(self):
        """
        Function to test the wifi on/off functionality
        pre-condition: screen turn on and unlock
        """
        result = self.my_device.turn_wifi(False)
        assert result
