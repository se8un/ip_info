import requests
import folium
from pyfiglet import Figlet


def get_info_by_id(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[status]': response.get('status'),
            '[country]': response.get('country'),
            '[lat]': response.get('lat'),
            '[lon]': response.get('lon'),
            '[regionName]': response.get('regionName'),
            '[countryCode]': response.get('countryCode'),
            '[timezone]': response.get('timezone'),
            '[zip]': response.get('zip'),
            '[org]': response.get('org'),
            '[as]': response.get('as')
        }

        for k, v in data.items():
            print(f'{k} : {v}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("country")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] check your connection!')


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    ip = input('enter a target IP: ')

    get_info_by_id(ip=ip)


if __name__ == '__main__':
    main()
