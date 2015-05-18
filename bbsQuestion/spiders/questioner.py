# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from scrapy.http import Request,FormRequest

import re
import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query
from scrapy import log
from scrapy.exceptions import DropItem

from  bbsQuestion.items import BbsquestionItem
from bbsQuestion import settings
import os

class QuestionerSpider(scrapy.Spider):
    name = "questioner"
    allowed_domains = ["bbs.byr.cn"]
    baseUrl = 'http://bbs.byr.cn'
    start_urls = (
        'http://www.bbs.byr.cn/',
    )
    def __init__(self,stats):
        self.stats = stats

        leancloud.init(settings.APP_ID_S, master_key=settings.MASTER_KEY_S)

        Boards = Object.extend('Boards')
        query = Query(Boards)
        query.exists('boardLink')
        query.select('boardLink')
        boards= query.find()
        self.urls = []
        for board in boards:
            self.urls.append(self.baseUrl+board.get('boardLink'))

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)

    def start_requests(self):
        # print "start_requests ing ......"
        # print self.urls
        for url in self.urls:
            yield Request(url,callback = self.parse)

    def parse(self, response):

        try:
            totalPageNum = int(response.xpath('//div[@class="t-pre-bottom"]//ul[@class="pagination"]//ol[@class="page-main"]/li[last()-1]/a/text()').extract()[0])
        except:
            totalPageNum = int(response.xpath('//div[@class="t-pre-bottom"]//ul[@class="pagination"]//ol[@class="page-main"]/li[last()]/a/text()').extract()[0])
        for index in range(1,totalPageNum+1):
            yield Request(response.url+"?p=" +str(index),callback = self.parsePage)
      #  print item['sectionListLink']

    def parsePage(self,response):
        item = BbsquestionItem()
        tbody = response.xpath('//div[@class="b-content"]//tbody')
        item['boardLink'] = "/board/"+re.split('board/(\w*)',response.url)[1]
        item['pageNum'] = int(re.split('(\d*)',response.url)[1])
        item['questionLinkList'] = tbody.xpath('//tr/td[1]/a/@href').extract()
        item['questionTypeList'] = tbody.xpath('//tr/td[1]//samp/@class').re('tag ico-pos-article-(\w*)')
        item['questionNameList'] = tbody.xpath('//tr/td[2]/a/text()').extract()
        item['questionReleaseDatetimeList'] = tbody.xpath('//tr/td[3]/text()').extract()
        item['questionAuthorLinkList'] = tbody.xpath('//tr/td[4]/a/@href').extract()
        item['questionAuthorIdList'] = tbody.xpath('//tr/td[4]/a/text()').extract()
        item['questionReplyCountList'] = tbody.xpath('//tr/td[5]/text()').extract()
        item['questionLastReplyLinkList'] = tbody.xpath('//tr/td[6]/a/@href').extract()
        item['questionLastReplyDatetimeList'] = tbody.xpath('//tr/td[6]/a/text()').extract()
        item['questionLastReplyIdLinkList'] = tbody.xpath('//tr/td[7]/a/@href').extract()
        item['questionLastReplyIdList'] = tbody.xpath('//tr/td[7]/a/text()').extract()
	
        return item

    def closed(self,reason):
        #f = open('../../nohup.out')
        #print f.read()
        leancloud.init(settings.APP_ID, master_key=settings.MASTER_KEY)

        try:
            nohupOut = open(os.getcwd()+'/nohup.out','r').read()
        except:
            nohupOut = "Cannot read nohup.out file"
        CrawlerLog = Object.extend('CrawlerLog')
        crawlerLog = CrawlerLog()

        crawlerLog.set('crawlerName',self.name)
        crawlerLog.set('crawlerLog',nohupOut)
        crawlerLog.set('closedReason',reason)
        crawlerLog.set('crawlerStats',self.stats.get_stats())
        try:
            crawlerLog.save()
        except:
            pass
