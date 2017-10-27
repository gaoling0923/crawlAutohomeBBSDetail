# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlautohomebbsdetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class AutohomeBbsSpiderItem(scrapy.Item):

    title = scrapy.Field()
    content = scrapy.Field()
    pub_time = scrapy.Field()

    author = scrapy.Field()
    author_url = scrapy.Field()
    reg_time = scrapy.Field()
    addr = scrapy.Field()
    attent_vehicle = scrapy.Field()
    jinghuatie = scrapy.Field()  # 精华帖
    fatieliang = scrapy.Field()  # 发帖量
    huitieliang=scrapy.Field() #回帖

    cdate = scrapy.Field()
    from_url = scrapy.Field()

    floor = scrapy.Field()
class QicheluntanDetail(scrapy.Item):
    title = scrapy.Field() #标题
    comenttext = scrapy.Field()  #内容
    author = scrapy.Field() #发帖用户
    url= scrapy.Field() #url
    bbsdate=scrapy.Field() #发帖时间
    replycount = scrapy.Field() #回复数
    liulancount = scrapy.Field()#浏览量
    jinghuadie=scrapy.Field() #精华帖
    fatieliang = scrapy.Field()#发帖量
    zhucedate = scrapy.Field()#注册日期
    useraddress = scrapy.Field()#用户地区
    suoshuzushi = scrapy.Field()#所属组织
    guanzhuche = scrapy.Field()#关注车
    aiche = scrapy.Field()#爱车
