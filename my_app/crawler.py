import requests
from requests.compat import quote_plus

import bs4
from typing import Union
from pyquery import PyQuery as pq

from .crawler_tool import CrawlerTool as tool


def save_html(html: str):
    with open('temp.html', 'w') as f:
        f.write(html)


class LACraigList:
    BASE_URL = 'https://losangeles.craigslist.org/search/?query={}'
    BASE_URL_WP = 'https://losangeles.craigslist.org/search/?query={}&min_price={}&max_price={}'

    @staticmethod
    def _str_to_int(s: str) -> Union[int, None]:
        if s.isnumeric():
            i = int(s)
            if i >= 0:
                return i

    @staticmethod
    def _parse_price(min_price_str: str, max_price_str: str) -> (Union[int, None], Union[int, None]):
        min_price = LACraigList._str_to_int(min_price_str)
        max_price = LACraigList._str_to_int(max_price_str)
        return min_price, max_price

    @staticmethod
    def _get_search_url(search_str: str, min_price: Union[int, None], max_price: Union[int, None]) -> str:
        search_f_str = quote_plus(search_str)
        if min_price and max_price:
            return LACraigList.BASE_URL_WP.format(search_f_str,
                                                  min_price,
                                                  max_price)
        else:
            return LACraigList.BASE_URL.format(search_f_str)

    @staticmethod
    def _extract_post():
        pass

    @staticmethod
    def _extract_nav_url(search_url: str, doc: pq):
        # get total post
        paginator_el = doc('div.paginator.buttongroup.firstpage > .buttons > .button.pagenum')
        first_post_in_page = int(paginator_el('.rangeFrom').text())
        last_post_in_page = int(paginator_el('.rangeTo').text())
        total_post = int(paginator_el('.totalcount').text())

        # first page url
        if first_post_in_page != 1:
            pass

    @staticmethod
    def _parse_doc(search_url: str, doc: pq):
        LACraigList._extract_nav_url(search_url, doc)
        pass

    @staticmethod
    def search(search_str: str, min_price_str: str, max_price_str: str):
        min_price, max_price = LACraigList._parse_price(min_price_str, max_price_str)
        search_url = LACraigList._get_search_url(search_str, min_price, max_price)
        print(f"search-url: {search_url}")

        response = tool.access(search_url)
        doc = tool.get_doc(response)
        LACraigList._parse_doc(search_url, doc)

        # print(html)
        # save_html(html)

    @staticmethod
    def search_with_url(search_url: str):
        pass
