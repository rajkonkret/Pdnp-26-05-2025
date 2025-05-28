import requests

# w terminalu
# pip install requests
url = 'https://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=json'

response = requests.get(url)
print(response)  # <Response [200]>
print(response.text)
# {"table":"A","currency":"euro","code":"EUR",
# "rates":[{"no":"102/A/NBP/2025","effectiveDate":"2025-05-28","mid":4.2447}]}
# 200 ok
# 3xx - przekierowania
# 4xx 404 - brak zasobu, 400 Bad Request
# 5xx bøedy po stronie serwera
data = response.json()
print(data)
print(type(data))

# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
#  'rates': [{'no': '102/A/NBP/2025', 'effectiveDate': '2025-05-28', 'mid': 4.2447}]}
print(data['rates'])  # [{'no': '102/A/NBP/2025', 'effectiveDate': '2025-05-28', 'mid': 4.2447}]
print(data['rates'][0])  # {'no': '102/A/NBP/2025', 'effectiveDate': '2025-05-28', 'mid': 4.2447}
print(data['rates'][0]['mid'])  # 4.2447
