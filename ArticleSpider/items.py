# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()、
    title=scrapy.Field()
    date=scrapy.Field()
    cas=scrapy.Field()
    text=scrapy.Field()
    #下载图片
    images_url=scrapy.Field()
    #图片路径
    images_path=scrapy.Field()
