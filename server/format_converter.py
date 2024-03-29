from datetime import datetime, timezone
import locale
import re


def get_locale_info(time: datetime):
    locale_time = time.strftime('%X')

    delimiter = re.findall(r'[^\d]', locale_time)
    return delimiter[0], delimiter[1]


def format_time(time: str, hour_delimiter: str, min_delimiter: str):
    # TODO: what about 24 hour places?
    # TODO: Are locale specific delimiters okay? 11.59:59 PM in assignment looks like a typo

    parts = time.split(" ")
    parts_int = [int(p) for p in parts[:-1]]
    assert len(parts) == 4

    # Remove leading zeros from hour part
    parts[0] = parts[0].lstrip("0").replace(" 0", "")

    if parts_int[1] == 0:
        if parts_int[2] == 0:
            del parts[1]
            del parts[1]
    elif parts_int[2] == 0:
        del parts[2]

    if len(parts) == 2:
        return ' '.join(parts)
    elif len(parts) == 3:
        return ' '.join(parts).replace(" ", hour_delimiter, 1)
    elif len(parts) == 4:
        return ' '.join(parts).replace(" ", hour_delimiter, 1).replace(" ", min_delimiter, 1)


class FormatConverter:
    def get_time(self, timestamp: str):
        # Explicitly set locale, this can be set on runtime to any supported locale
        locale.setlocale(locale.LC_ALL, 'en-029.utf8')

        assert int(timestamp) <= 86399
        time = datetime.fromtimestamp(int(timestamp), tz=timezone.utc)
        return format_time(f'{time:%I %M %S %p}', *get_locale_info(time))
