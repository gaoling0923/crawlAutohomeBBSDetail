# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from crawlAutohomeBBSDetail.items import AutohomeBbsSpiderItem


class CrawlautohomebbsdetailPipeline(object):
    def process_item(self, item, spider):
        return item

class b30bbsPipeline(object):
    def __init__(self):
        self.filedetail = open('D:/crawlfiles/yiqib30/b30_detail.txt', 'wb');
    def process_item(self, item, spider):
        vaild = True
        if item is not None:
            if isinstance(item, AutohomeBbsSpiderItem):
                line = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (item['title'],
                                                                   item['content'],
                                                                   item['pub_time'],
                                                                   item['author'],
                                                                   item['author_url'],
                                                                   item['reg_time'],
                                                                   item['jinghuatie'],
                                                                   item['fatieliang'],
                                                                   item['huitieliang'],
                                                                   item['addr'],
                                                                   item['attent_vehicle'],
                                                                   item['from_url'],
                                                                   item['floor'])
                self.filedetail.write(line.encode("utf-8"))
                return item
            else :

                print('execute data insert file')

                line = "%s\t%s" % (item['comenttext'],item['bbsdate'])
                self.filedetail.write(line.encode("utf-8"))
                return item

        else :
            item