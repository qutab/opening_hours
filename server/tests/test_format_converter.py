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
