import call_api
import json
import csv

api_data = call_api.api_call('reports/list', {})
jsonResponse = json.loads(api_data.decode('utf-8'))
file_data = (jsonResponse[0])
for key, value in file_data.items():
    if 'csv' in value:
        csv_file = value
        print(csv_file)

