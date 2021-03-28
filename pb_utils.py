from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import datetime
import re
import uuid


def get_source_from_url(url, logger):
    logger.info('getting source from url')

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(url)
    return browser.page_source


def find_movies(source, logger):
    logger.info('finding items')

    pattern = re.compile(r'.*?id="st">\n.*?item-title">.*?>(.*?)</a>.*?item-uploaded">(.*?)</span>'
                         + r'.*?"item-icons".*?href="(.*?)".*?item-size">(\d+.\d+)\S\w+\S(\w+).*?', re.S)
    items = re.findall(pattern, source)
    now = datetime.datetime.now()

    for item in items:
        yield{
            'id': str(uuid.uuid4()),
            'title': item[0].replace("'", ''),
            'magnet': item[2],
            'last_updated': now.strftime('%Y-%m-%d %H:%M:%S')
        }
