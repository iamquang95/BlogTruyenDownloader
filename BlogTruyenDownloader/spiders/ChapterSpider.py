# -*- coding: utf-8 -*-
import json
import scrapy
from BlogTruyenDownloader.items import ChapterItem


class ChapterSpider(scrapy.Spider):
    name = "chapter"
    allowed_domains = ["blogtruyen.com"]
    start_urls = []
    with open('ListComic.json') as list_comics_file:
        try:
            list_comics = json.load(list_comics_file)
        except ValueError:
            list_comics = []

    for i in xrange(0, len(list_comics)):
        list_chapter = list_comics[i]['link_chapters']
        for j in xrange(0, len(list_chapter)):
            start_urls.append("http://blogtruyen.com" + str(list_chapter[j]))

    i_url = 0

    def parse(self, response):
        item = ChapterItem()
        item['name'] = ChapterSpider.list_comics[ChapterSpider.i_url]['name']
        item['chap'] = response.xpath('//header/h1/text()')[0].extract()
        item['images'] = []
        for image in response.xpath('//article[@id="content"]/img'):
            item['images'].append(image.xpath('@src')[0].extract())
        yield item
