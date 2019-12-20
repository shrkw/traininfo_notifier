from typing import Tuple

import requests
from lxml import html


class YahooTrainInfoScraper:
    def fetch_train_info(self, yahoo_train_info_url: str) -> Tuple[str, str]:
        page = requests.get(yahoo_train_info_url)
        tree = html.fromstring(page.content)

        element_title = tree.xpath("//h1[@class='title']")
        element_status = tree.xpath("//div[@id='mdServiceStatus']")
        title = element_title[0].text_content()

        status = element_status[0].text_content()
        return title, status


if __name__ == "__main__":
    sc = YahooTrainInfoScraper()
    sc.fetch_train_info("https://transit.yahoo.co.jp/traininfo/detail/84/0/")
    pass
