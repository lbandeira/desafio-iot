import requests

url = "https://raw.githubusercontent.com/eusouagabriel/desafio-iot/main/devices.json"
response = requests.get(url)

if response.status_code == 200:
  devices = response.json()
  print(devices)
else:
  print("Failed to retrieve data")
