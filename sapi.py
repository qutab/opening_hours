import schemapi

schema = {
  "definitions": {
    "time_entry": {
      "type": "array",
      "properties": {
        "type": { "type": "string" },
        "value": { "type": "string" }
      },
      "required": ["type", "value"]
    }
  },

  "type": "object",

  "properties": {
    "monday": { "$ref": "#/definitions/time_entry" },
    "tuesday": { "$ref": "#/definitions/time_entry" },
    "wednesday": { "$ref": "#/definitions/time_entry" },
    "thursday": { "$ref": "#/definitions/time_entry" },
    "friday": { "$ref": "#/definitions/time_entry" },
    "saturday": { "$ref": "#/definitions/time_entry" },
    "sunday": { "$ref": "#/definitions/time_entry" }
  },
  
  "required": ["friday", "saturday"]
}

api = schemapi.SchemaModuleGenerator(schema, root_name='OpeningHours')
api.write_module('myschema.py')

