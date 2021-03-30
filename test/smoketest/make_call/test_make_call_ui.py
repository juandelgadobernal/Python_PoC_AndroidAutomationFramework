"""Test make call ui Module"""
# pylint: disable=E1101,R0903
import pytest

@pytest.mark.integration_tests
class TestMakeCallUi():
    """Test make call with UI"""
    def test_make_call_ui(self):
        """
        Function to test the phonecall using UI
        Pre-conditions: Phone unlock
        phone in home page
        phone app need to be in the home page
        """
        result = self.my_device.make_phone_call_ui(self.phone_number)
        assert result
