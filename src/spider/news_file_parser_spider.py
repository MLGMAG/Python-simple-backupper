import scrapy
import os
import re

# scrapy crawl news_file_parser -O ./result.json

CURRENT_DIR_PATH = os.path.abspath(os.getcwd())
BASE_URL = "https://lb.ua/news/2024/02/16"

def make_url(filename):
    return f"file://{CURRENT_DIR_PATH}/resources/{filename}"

def _sanitize_element(element):
    return element.strip()

def _filter_element(element):
    return len(element) > 0

def _add_punctuation_padding(text):
    text = re.sub('([.,!?()\"`“”:«»])', r' \1 ', text)
    text = re.sub('\s{2,}', ' ', text)
    return text

def get_article_title(response):
    article_title_raw = response.css('h1[itemprop="headline"]::text').get()
    article_title_sanitized = _sanitize_element(article_title_raw)
    return _add_punctuation_padding(article_title_sanitized)

def get_link(response):
    page = response.url.split('/')[-1]
    return f'{BASE_URL}/{page}'

def get_text(response):
    text_chunks = response.css('div[itemprop="articleBody"] *::text').extract()
    sanitized_text_chunks = list(map(_sanitize_element, text_chunks))
    filtered_text_chunks = list(filter(_filter_element, sanitized_text_chunks))
    text = " ".join(filtered_text_chunks)
    return _add_punctuation_padding(text)

class NewsSpider(scrapy.Spider):
    name = "news_file_parser"

    def __init__(self, category='', **kwargs):
        files_in_resources = os.listdir('./resources')
        current_dir_path = os.path.abspath(os.getcwd())
        self.start_urls = list(map(make_url, files_in_resources))

        super().__init__(**kwargs)

    def parse(self, response):
        yield {
            'article': get_article_title(response),
            'link': get_link(response),
            'header': get_article_title(response),
            'text': get_text(response)
        }
