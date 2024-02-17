from typing import Self
from unittest import TestCase

from app.ip_utils import get_ip_location, is_ip_address, lambda_handler


class TestApp(TestCase):
    def test_is_ip_address(self: Self) -> None:
        # Assemble
        sample_data = "1.1.1.1"
        # Action
        is_ip = is_ip_address(sample_data)
        # Assert
        self.assertTrue(is_ip)

    def test_get_ip_location(self: Self) -> None:
        # Assemble
        sample_data = "2.2.2.2"
        # Action
        actual_location = get_ip_location(sample_data)
        # Assertion
        expected_location = {
            "lat": float,
            "lon": float,
            "city": str,
            "country": str,
        }
        for field_name, value_type in expected_location.items():
            self.assertIn(field_name, actual_location)
            self.assertIsInstance(actual_location[field_name], value_type)

    def test_lambda_handler(self: Self) -> None:
        # Assemble
        sample_data = {"event": {"ip_address": "3.3.3.3"}, "context": {}}

        # Action
        actual_response = lambda_handler(**sample_data)

        # Assertion
        expected_location = {
            "lat": float,
            "lon": float,
            "city": str,
            "country": str,
        }
        for field_name, value_type in expected_location.items():
            self.assertIn(field_name, actual_response)
            self.assertIsInstance(actual_response[field_name], value_type)
