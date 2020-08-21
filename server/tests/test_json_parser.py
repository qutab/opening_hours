import pytest
from server.json_parser import *

short_str = """
{
    "monday" : [
        {
            "type" : "open",
            "value" : 64800
        }
    ]
}
"""


@pytest.fixture
def uut():
    return JsonParser()


def test_format_conversion(uut):
    test_str = """ {
        "friday" : [
            {
                "type" : "open",
                "value" : 64800
            }
        ],
        "saturday": [
            {
                "type" : "close",
                "value" : 3600
            },
            {
                "type" : "open",
                "value" : 32400
            },
            {
                "type" : "close",
                "value" : 39600
            },
            {
                "type" : "open",
                "value" : 57600
            },
            {
                "type" : "close",
                "value" : 82800
            }
        ]
    }
    """

    expected_str = """A restaurant is open:
Friday: 6 PM - 1 AM
Saturday: 9 AM - 11 AM, 4 PM - 11 PM"""
    assert uut.parse(test_str) == expected_str
