from unittest import TestCase

from app.ip_utils import is_ip_address


class TestApp(TestCase):
    def test_is_ip_address(self):
        # Assemble
        sample_data = "1.1.1.1"
        # Action
        is_ip = is_ip_address(sample_data)
        # Assert
        self.assertTrue(is_ip)
