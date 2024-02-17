import ipaddress

import requests


def is_ip_address(value: str) -> bool:
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False


def get_ip_location(value: str) -> dict[str, str | float]:
    if not is_ip_address(value):
        raise ValueError("The value is not an IP!")

    response = requests.get(f"http://ip-api.com/json/{value}", timeout=30)
    response.raise_for_status()

    response_data = response.json()

    return {
        "lat": response_data.get("lat"),
        "lon": response_data.get("lon"),
        "city": response_data.get("city"),
        "country": response_data.get("country"),
    }
