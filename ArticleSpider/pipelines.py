# -*- coding: utf-8 -*-
import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.pipelines.images import ImagesPipeline
class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item
#获取文章封面在本地的路经
class Articl_image_path_Pipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok,images_path in results:
            dic_images_path=images_path
        item['images_path']=dic_images_path['path']
        return item
#自定义一个pipeline用来把item里面的数据持久化到json文件中
class Article_json_pipeline(object):
    def __init__(self):
        self.file=codecs.open("article.json","w",encoding="utf-8")
    def process_item(self, item, spider):
        line=json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(line)
        return item