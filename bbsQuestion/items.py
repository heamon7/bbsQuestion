# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BbsquestionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    boardName = scrapy.Field()
    pageNum= scrapy.Field()
    questionLinkList= scrapy.Field()
    questionTypeList= scrapy.Field()
    questionNameList= scrapy.Field()
    questionReleaseDatetimeList= scrapy.Field()
    questionAuthorLinkList= scrapy.Field()
    questionAuthorIdList= scrapy.Field()
    questionReplyCountList= scrapy.Field()
    questionLastReplyLinkList= scrapy.Field()
    questionLastReplyDatetimeList= scrapy.Field()
    questionLastReplyIdLinkList= scrapy.Field()
    questionLastReplyIdList= scrapy.Field()
