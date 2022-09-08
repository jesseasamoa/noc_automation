import call_api
import json

print(call_api.api_call('reports/subscribed', {}))
# api_data = call_api.api_call('reports/types', {})
#
# with open(api_data) as json_file:
#     data = json.load(json_file)
#     print(data)