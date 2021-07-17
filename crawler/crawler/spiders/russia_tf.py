import scrapy
from scrapy.http import Request
from crawler.items import Article
from w3lib.html import remove_tags

from datetime import datetime


class RussiaTfSpider(scrapy.Spider):
    name = 'russia_tf'
    allowed_domains = ['russia24.pro']
    start_urls = ['https://russia24.pro/news/']

    def parse(self, response):
        # проход по новым статьям
        article_urls = response.xpath("//div[@class='r24NewsList']//div[@class='r24_body']//@href").extract()
        for article_url in article_urls:
            yield Request(article_url, callback=self.parse_article)

    def parse_article(self, response):
        # парсинг статьи
        title = response.xpath("//div[@id='r24Article']//header/h1/text()").extract_first()
        location = response.xpath("//div[@id='r24Container']//span[@class='r24_title']/text()").extract_first()
        text_lines = response.xpath("//div[@class='r24_text']/p//text()").extract()
        if not text_lines:
            text_lines = response.xpath("//div[@class='r24_text']//text()").extract()

        text = ''
        for line in text_lines:
            text += line.strip()

        source_selector = response.xpath("//div[@class='r24_source']")
        source = source_selector.xpath(".//a/text()").extract_first()
        source_url = source_selector.xpath(".//@href").extract_first()

        date = datetime.fromisoformat(response.xpath("//div[@class='r24_info']//@datetime").extract_first())

        article = Article()
        article['title'] = title
        article['location'] = location
        article['text'] = text
        article['source'] = source
        article['source_url'] = source_url
        article['date'] = date.strftime("%d.%m.%Y %H:%M:%S")

        yield article