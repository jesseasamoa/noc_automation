import call_api
import json

# print(call_api.api_call('reports/types', {}))
api_data = call_api.api_call("reports/types", {})
jsonResponse = json.loads(api_data.decode('utf-8'))
print(jsonResponse)
# print(type(api_data))
#
# with open(api_data) as json_file:
#     data = json.load(json_file)
#     print(data)