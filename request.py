import requests
from helpers import print_comment

url = 'http://localhost:8081/weight'

request = {
    'Species': 'Bream',
    'Length1': 24.5,
    'Length2': 27,
    'Length3': 30.2,
    'Height': 11.2,
    'Width': 3.9
}

print_comment('Sending request')
print(request)

response = requests.post(url,json=request)

print_comment('Recieved response: ' + str(response.status_code))
print(response.json())