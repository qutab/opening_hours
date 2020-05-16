import pytest
from server.format_converter import *


@pytest.fixture
def uut():
    return FormatConverter()


def test_time_conversion(uut):
    assert uut.get_time("64800") == "6 PM"
    assert uut.get_time("64801") == "6:00:01 PM"
    assert uut.get_time("64860") == "6:01 PM"
    assert uut.get_time("64861") == "6:01:01 PM"

    assert uut.get_time("0") == "12 AM"
    assert uut.get_time("1") == "12:00:01 AM"
    assert uut.get_time("60") == "12:01 AM"
    assert uut.get_time("61") == "12:01:01 AM"
    assert uut.get_time("3600") == "1 AM"

    assert uut.get_time("32400") == "9 AM"
    assert uut.get_time("39600") == "11 AM"
    assert uut.get_time("57600") == "4 PM"
    assert uut.get_time("82800") == "11 PM"
    assert uut.get_time("37800") == "10:30 AM"
    assert uut.get_time("86399") == "11:59:59 PM"


def test_format_conversion(uut):
    test_str = """
{
    "friday" : [
        {
            "type" : "open",
            "value" : 64800
        }
    ],
    “saturday”: [
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
    expected_str = """
A restaurant is open:
Friday: 6 PM - 1 AM
Saturday: 9 AM -11 AM, 4 PM - 11 PM
"""
    assert uut.get_output(test_str) == expected_str
