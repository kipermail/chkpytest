POST_SCHEMA = {
    "type": "object",
    "properties": {
        "one": {"type": "string", "enam": "one"},
        "key": {"type": "string", "enam": "key"},
    },
    "required": ["one", "key"],
    "additionalProperties": False
}
# {'one': 'two', 'key': 'value'}