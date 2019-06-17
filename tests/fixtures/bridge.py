"""Define fixtures for bridges."""
import pytest


@pytest.fixture()
def bridge_all_json():
    """Define a response to GET /base_stations."""
    return {
        "base_stations": [
            {
                "id": 12345,
                "name": None,
                "mode": "home",
                "hardware_id": "0x1234567890abcdef",
                "hardware_revision": 4,
                "firmware_version": {
                    "wifi": "0.121.0",
                    "wifi_app": "3.3.0",
                    "silabs": "1.0.1",
                },
                "missing_at": None,
                "created_at": "2019-04-30T01:43:50.497Z",
                "updated_at": "2019-04-30T01:44:43.749Z",
                "system_id": 12345,
                "firmware": {"wifi": "0.121.0", "wifi_app": "3.3.0", "silabs": "1.0.1"},
                "links": {"system": 12345},
            }
        ]
    }
