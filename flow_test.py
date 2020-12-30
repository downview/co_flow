import requests
import json

    
field1 = 'stationName'
field2 = 'measValue'
field3 = 'PLAHARCO'

base_url = f"https://dwr.state.co.us/"

endpoint_path = f"Rest/GET/api/v2/telemetrystations/telemetrystation/?fields={field1}%2C{field2}&abbrev={field3}"

endpoint= f'{base_url}{endpoint_path}'

r = requests.get(endpoint)

print(r.json())

