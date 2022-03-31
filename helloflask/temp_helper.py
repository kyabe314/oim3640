import urllib.request
import json
import pprint

def get_temp(city):
    city = city.replace(' ', '%20')
    APIKEY = '3bada50fc4b8667695d10d85e01d661f' # import from another file to hide sensitive information
    city = 'Wellesley'
    country_code = 'us'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

    # print(url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # print(response_data)

    # pprint.pprint(response_data)
    # How do we get current temperature?
    # print(response_data['main']['temp'], 'Kelvin')
    temp = response_data['main']['temp']
    return temp - 273.15

def main():
    print(get_temp('Wellesley'))

if __name__ == '__main__':
    main()