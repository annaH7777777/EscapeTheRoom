#Which file format is commonly used for Python serialization?
#JSON

import json

# Python object → JSON string (serialization)
data = {"name": "Anna", "scores": [95, 87, 92]}
json_string = json.dumps(data)
print(json_string)  # → '{"name": "Anna", "scores": [95, 87, 92]}'

# JSON string → Python object (deserialization)
restored = json.loads(json_string)
print(restored["name"])  # → Anna