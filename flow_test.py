# API request to Colorado Steam Gauges on the South Platte River

import requests
import json

# Arguments for the request.
# field1 returns the full name of the stream gauge 
# field2 is the flow measurment in cubin feet per second (cfs)
# field3 is the abbreviation for the requested stream gauge

field1 = 'stationName'
field2 = 'measValue'
field3 = 'PLAHARCO'

base_url = f"https://dwr.state.co.us/"

endpoint_path = f"Rest/GET/api/v2/telemetrystations/telemetrystation/?fields={field1}%2C{field2}&abbrev={field3}"

endpoint= f'{base_url}{endpoint_path}'

r = requests.get(endpoint)

print(r.json())

