# -*- coding: utf-8 -*-

import scrapy


class ComicItem(scrapy.Item):
    name = scrapy.Field()
    link_chapters = scrapy.Field()


class ChapterItem(scrapy.Item):
    name = scrapy.Field()
    chap = scrapy.Field()
    images = scrapy.Field()
