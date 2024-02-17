from unittest import TestCase

from app.ip_utils import is_ip_address, get_ip_location


class TestApp(TestCase):
    def test_is_ip_address(self):
        # Assemble
        sample_data = "1.1.1.1"
        # Action
        is_ip = is_ip_address(sample_data)
        # Assert
        self.assertTrue(is_ip)

    def test_get_ip_location(self):
        # Assemble
        sample_data = "2.2.2.2"
        # Action
        actual_location = get_ip_location(sample_data)
        # Assertion
        expected_location = {
            "lat": 48.8566,
            "lon": 2.35222,
            "city": "Paris",
            "country": "France",
        }
        self.assertEqual(expected_location, actual_location)
