# -*- coding: utf-8 -*-
import scrapy
import re
from news_spider.items import News

class NeteaseSpiderSpider(scrapy.Spider):
    name = "netease_spider"
    PAGE_SIZE = 25
    start_urls = ['http://3g.163.com/touch/article/list/BBM54PGAwangning/0-5000.html']
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
     (KHTML, like Gecko) Ubuntu Chromium/56.0.2924.76 Chrome/56.0.2924.76 Safari/537.36"}
    news_count = 0

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], headers=self.header, callback=self.parse)

    def parse(self, response):
        content = response.xpath('//body/p/text()').extract()[0]
        # with io.open('news.txt', 'w') as f:
        #     f.write(content)
        urls = re.findall(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            content)

        for url in urls:
            if url.endswith('html'):
                yield scrapy.Request(url=url, callback=self.parse_news)


    def parse_news(self, response):
        item = News()
        item['title'] = response.xpath('/html/body/h1/text()').extract()[0]
        content = ''
        ps = response.xpath('//body/div[@class="content"]/p')
        for p in ps:
            content += p.xpath('./text()').extract()[0]
        item['content'] = content

        return item






