# API request to Colorado Steam Gauges on the South Platte River

import requests
import json

# Arguments for the request.
# field1 returns the full name of the stream gauge 
# field2 is the flow measurment in cubic feet per second (cfs)
# field3 is the abbreviation for the requested stream gauge

field1 = 'stationName'
field2 = 'measValue'
field3 = 'PLAHARCO,PLACHECO,PLAGEOCO,MFKSTMCO,'

base_url = f"https://dwr.state.co.us/"

endpoint_path = f"Rest/GET/api/v2/telemetrystations/telemetrystation/?fields={field1}%2C{field2}&abbrev={field3}"

endpoint= f'{base_url}{endpoint_path}'

response = requests.get(endpoint)

# Clean up the output to make it readable

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Only return the Station Name & Stream Flow in cfs

flows  = response.json()['ResultList']

jprint(flows)
