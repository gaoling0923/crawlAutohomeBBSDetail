# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
from crawlAutohomeBBSDetail.items import QicheluntanDetail


class Crawlb30bbsdetailSpider(CrawlSpider):
    name = 'crawlb30bbsdetail'
    allowed_domains = ['club.autohome.com.cn']
    start_urls = ['http://club.autohome.com.cn/bbs/forum-c-3695-1.html/']
    count=0;
   # log.start(logfile='D:/crawlfiles/yiqib30/bbs.log', loglevel=log.INFO, logstdout=True);

    rules = (
        #Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),

        #http://club.autohome.com.cn/bbs/thread-a-3695-66215235-1.html

        Rule(LinkExtractor(allow='http://club.autohome.com.cn/bbs/thread-*', restrict_css=('.a_topic')),callback='parse_content', follow=True),

    )


    def parse_content(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        self.count = self.count + 1
        #coments = response.css('.contstxt')
        coments =soup.select('.clearfix.contstxt.outer-section')
        print('主页==',coments);
        #for sub in coments:
            #i = QicheluntanDetail();
            #print('excute url:', sub.select('#consnav > span')[0].get_text());
            #i['title'] = sub.select('.w740 .tz-paragraph div')[0].get_text(strip=True);
             #print('回复sapz==',sub.select('.plr26 .rtopconnext'))
           # i['bbsdate'] = sub.select('#F0 > div.conright.fr > div.plr26.rtopcon > span:nth-child(4)')[0].get_text(strip=True);
            #print('excute count==', self.count);

            #yield i;
        #next = soup.select('#consnav > span:nth-child(4)')[0].get_text(strip=True);
        #url = response.urljoin(next);
        # print('下一页', url);
        #print('次数', self.count);
        #yield scrapy.Request(url=url, callback=self.parse_content);

    def parse_content3(self, response):
        self.count = self.count + 1
        #coments = response.css('.contstxt')
        coments = response.css('.clearfix.contstxt.outer-section')
        print(coments);
        for sub in coments:
            i = QicheluntanDetail();
            i['comenttext'] = sub.css('w740::text').extract_first();
            datespan= sub.css('.plr26.rtopconnext span').extract;

            print('时间===',datespan.css(''));
            i['bbsdate'] = '456';
            print('excute count==', self.count);
            print('帖子内容:', sub.css('.rtitle .maxtitle::text').extract_first())
            yield i;
        next = response.css('.afpage::attr(href)').extract_first();
        url = response.urljoin(next);
        # print('下一页', url);
        print('次数', self.count);
        yield scrapy.Request(url=url, callback=self.parse_content);



