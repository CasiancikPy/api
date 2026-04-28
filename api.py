import requests


def main():
    cities = ['Лондон', 'Аэропорт Шереметьево', 'Череповец']

    for city in cities:
        url_template = "https://wttr.in/{}"
        url = url_template.format(city)
        playout = {
            'lang': 'ru',
            'T': '',
            'M': '',
            'n3': '',
            '3': '',
            'q': ''
        }
        response = requests.get(url, params=playout)
        response.encoding = 'utf-8'
        print(response.text)


if __name__ == '__main__':
    main()