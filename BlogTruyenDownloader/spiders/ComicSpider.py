# -*- coding: utf-8 -*-

import scrapy
from BlogTruyenDownloader.items import ComicItem


class ComicSpider(scrapy.Spider):
    name = "comic"
    allowed_domains = ["blogtruyen.com"]
    with open("link_comic.txt", "r") as f:
        try:
            start_urls = f.read().split()
        except Exception, ValueError:
            start_urls = []

    def parse(self, response):
        comic_name = response.xpath('//div[@id="breadcrumbs"]')
        comic_name = comic_name.xpath('span/text()')
        comic_name = comic_name[1].extract()
        chapters = response.xpath('//div[@id="list-chapters"]')
        url_chapters = chapters.xpath('p/span/a/@href').extract()
        item = ComicItem()
        item['name'] = comic_name
        item['link_chapters'] = url_chapters
        yield item
