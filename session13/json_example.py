import urllib.request
import json

APIKEY = '3bada50fc4b8667695d10d85e01d661f'
city = 'Wellesley'
country_code = 'us'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
# print(response_data)

# How do we get current temperature?
print(response_data['main']['temp'], 'Kelvin')