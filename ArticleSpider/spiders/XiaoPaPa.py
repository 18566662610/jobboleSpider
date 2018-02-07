# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http import Request
from ArticleSpider.items import ArticlespiderItem


'''
    简介：
        名字：小爬爬
        功能：一只爱好学习python的小蜘蛛，爬取伯乐在线关于python的技术文章
'''
class XiaopapaSpider(scrapy.Spider):
    name = 'XiaoPaPa'
    allowed_domains = ['python.jobbole.com/all-posts']
    #文章列表首页：开始索引
    start_urls = ['http://python.jobbole.com/all-posts/']
    #解析索引url
    def parse(self, response):
        #获取文章列表页中的每个列表的的节点 节点下有url和封面图
        all_text_pagesNode=response.xpath("//*[@id='archive']//div[@class='post floated-thumb']/div[1]")
        #获取文章列表页中的每篇文章的封面图的url
        #images_url=response.xpath("//*[@id='archive']//div[@class='post floated-thumb']/div[1]/a[1]/img/@src").extract()
        #每个url将调用解析具体文章的方法去解析详情页然后把文章列表的封面也传入
        for index in all_text_pagesNode:
            #单个文章页的url
            index_text_page=index.xpath("a/@href").extract_first()
            print(index_text_page)
            images_url=index.xpath("a[1]/img/@src").extract_first()
            print(images_url)
            #文章列表中每篇文章的url传给专门解析文章详情页的方法去解析
            yield Request(url=index_text_page,callback=self.parse_detail,dont_filter=True,meta={"images_url":images_url})
        print("测试用---------------------整页20个url已经解析完成")
        print(("测试用---------------------"+"继续解析下一页文章列表的所有url come on"))
        #获取完列表获取下一页文章列表页的url
        next_text_page=response.xpath("//a[@class='next page-numbers']/@href").extract_first()
        #如果有下一页解析下一页的url传给初始解析器parse解析递归使用
        if next_text_page:
            yield  Request(url=next_text_page,callback=self.parse,dont_filter=True)
        print("测试用---------------------"+"come 下一页 不要停")

    ######解析具体的文章详情页面
    def parse_detail(self, response):
        article_item=ArticlespiderItem()
        #解析获取文章的标题
        title=response.xpath("//div[@class='entry-header']/h1/text()").extract_first()
        article_item["title"]=title
        print("测试用---------------------"+title)
        #解析获取文章的发表日期
        date=response.xpath("//div[@class='grid-8']/div[1]/div[2]/p[1]/text()").extract_first().strip()[0:10]
        article_item["date"]=date
        print("测试用---------------------"+date)
        #解析文章来自于哪个分类//p[@class='entry-meta-on-mobile']
        cas=response.xpath("//div[@class='grid-8']/div[1]/div[2]/p[1]/a[1]/text()").extract_first()
        article_item["cas"]=cas
        print("测试用---------------------"+cas)
        #获取文章的封面图url
        images_url=response.meta.get('images_url','')
        # 将文章的封面图传给item
        article_item["images_url"]=[images_url]
        #解析文章的正文
        text=response.xpath("//div[@class='entry']//text()").extract()
        article_item["text"]=text
        print("测试用---------------------"+'正文不打印了')
        yield article_item



