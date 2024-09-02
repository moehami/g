import requests

# Get response.
response = requests.request(
    'GET',
    'http://data.oxylabs.io/v1/queries/{job_id}/results',
    auth=('moehamid', 'Enterne@24')
)

# This will return the JSON response with results.
print(response.json())
