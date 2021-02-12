import requests
from requests.compat import quote_plus
import bs4


def save_html(html: str):
    with open('temp.html', 'w') as f:
        f.write(html)


class LACraigList:
    BASE_URL = 'https://losangeles.craigslist.org/search/?query={}'

    @staticmethod
    def search(s: str):
        search_url = LACraigList.BASE_URL.format(quote_plus(s))
        response = requests.get(search_url)
        html = response.text
        # print(html)
        save_html(html)
