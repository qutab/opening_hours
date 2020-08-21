import python_jsonschema_objects as pjs
from .oh_calculator import *

schema_opening_hours = {
    "title": "Opening Hour Schema",
    "definitions": {
        "time_entry": {
            "title": "Time Entry",
            "type": "object",
            "properties": {
                "type": {"type": "string"},
                "value": {"type": "number"}
            },
            "required": ["type", "value"]
        },
        "day_entry": {
            "type": "array",
            "items": {"$ref": "#/definitions/time_entry"},
            "maxItems": 7,
            "uniqueItems": True,  # TODO: Can there be duplicate entries?
            "default": []
        }
    },

    "type": "object",

    "properties": {
        "monday": {"$ref": "#/definitions/day_entry"},
        "tuesday": {"$ref": "#/definitions/day_entry"},
        "wednesday": {"$ref": "#/definitions/day_entry"},
        "thursday": {"$ref": "#/definitions/day_entry"},
        "friday": {"$ref": "#/definitions/day_entry"},
        "saturday": {"$ref": "#/definitions/day_entry"},
        "sunday": {"$ref": "#/definitions/day_entry"}
    },

    "additionalProperties": False
}


class JsonParser:
    def __init__(self):
        builder = pjs.ObjectBuilder(schema_opening_hours)
        self.classes = builder.build_classes(named_only=True)
        self.opening_hours = self.classes.OpeningHourSchema

    def get_data(self):
        return self.opening_hours

    def parse(self, input_str: str):
        '''
        :param input_str: opening hours in json format
        :return: internal representation of the parsed json opening hours data
        '''
        opening_hours = self.opening_hours.from_json(input_str)
        # ensure that order is the same, #todo check if this is gauranteed by the schema somehow
        assert (list(opening_hours.keys()) == DAYS_OF_WEEK)

        # Create internal representation
        # Array of arrays containing open, close timings for each day
        # e.g. [[], [], [], [], [('open', '64800')], [('close', '3600'), ('open', '32400'), ('close', '39600')], []]
        parsed_data = []
        for day, timings in opening_hours.items():
            parsed_data.append([])
            if timings:
                for time in timings:
                    parsed_data[-1].append((str(time.type), str(time.value)))

        return get_output(parsed_data)
