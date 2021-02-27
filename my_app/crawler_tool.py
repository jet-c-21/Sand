"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/27/21
"""
# coding: utf-8
import requests
from requests.models import Response
from pyquery import PyQuery as pq


class CrawlerTool:
    @staticmethod
    def access(url: str) -> Response:
        try:
            return requests.get(url)
        except Exception as e:
            msg = f"failed to access page. url: {url} Error: {e}"
            print(msg)

    @staticmethod
    def get_doc(response: Response) -> pq:
        return pq(response.text)
