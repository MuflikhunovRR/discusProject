import json
import genson

builder = genson.SchemaBuilder()

json_body = {}

builder.add_object(json_body)

print(json.dumps(builder.to_schema(), indent=2))