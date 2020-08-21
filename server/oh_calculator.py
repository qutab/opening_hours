import itertools
from .format_converter import *
import logging

# TODO: use calendar module for this?
DAYS_OF_WEEK = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];
SEPARATOR = ', '


def pairwise(iterable):
    _first, _next = itertools.tee(iterable)
    next(_next, None)
    return zip(_first, _next)


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def is_closed_next_day(items):
    if items:
        return items[-1][0] == 'open'


def handle_multiple_day_span(parsed_data):
    for first, second in pairwise(parsed_data):
        if is_closed_next_day(first):
            first.append(second[0])
            second.pop(0)


def is_valid_data(opening, closing):
    assert opening[0] == 'open'
    assert closing[0] == 'close'


def get_output(parsed_data):
    handle_multiple_day_span(parsed_data)

    result_str = "A restaurant is open:"

    converter = FormatConverter()
    for day, timing in zip(DAYS_OF_WEEK, parsed_data):
        res = ""
        if not timing:
            continue

        for opening, closing in grouper(timing, 2):
            try:
                is_valid_data(opening, closing)
            except AssertionError:
                logging.error("Opening and closing times are not in expected order")
                return ""

            res += converter.get_time(opening[1]) + ' - ' + converter.get_time(closing[1]) + SEPARATOR

        result_str += '\n' + day.capitalize() + ': ' + res.rstrip(SEPARATOR)

    return result_str.rstrip()
