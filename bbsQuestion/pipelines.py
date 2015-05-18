# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query
from scrapy import log
from scrapy.exceptions import DropItem
from bbsQuestion import settings
import time


class QuestionPipeline(object):
    def __init__(self):
        dbPrime = 97
        leancloud.init(settings.APP_ID, master_key=settings.MASTER_KEY)

    def process_item(self, item, spider):
        tableIndex = int(1000*time.time())%self.dbPrime
        if tableIndex<10:
            tableIndexStr = '0' +str(tableIndex)
        else :
            tableIndexStr = str(tableIndex)

        Questions = Object.extend('Questions'+tableIndexStr)
        QuestionInfo = Object.extend('QuestionInfo'+tableIndexStr)


        for index ,ques in enumerate(item['questionLinkList']):
            question = Questions()
            questionInfo = QuestionInfo()
            # query = Query(Questions)
            # queryInfo = Query(QuestionInfo)
            # query.equal_to('questionLink',item['questionLinkList'][index])
            try:
                # if query.find():
                if 1:
                    pass
                else:

                    question.set('boardId',re.split('/board/',item['boardLink'])[1])
                    # question.set('pageNum',item['pageNum'])
                    question.set('questionLink',item['questionLinkList'][index])
                    # question.set('questionName',item['questionNameList'][index])
                    question.set('questionReleaseDatetime',item['questionReleaseDatetimeList'][index])
                    # question.set('questionAuthorLink',item['questionAuthorLinkList'][index])
                    question.set('questionAuthorId',item['questionAuthorIdList'][index])
                    try:
                        question.save()

                    except LeanCloudError,e:
                        print e
            except LeanCloudError,e:
                print e
            
            # queryInfo.equal_to('questionLink',item['questionLinkList'][index])
            # queryInfo.equal_to('questionReplyCount',int(item['questionReplyCountList'][index]))
            try:
                # if queryInfo.find():
                if 1:
                    pass
                else:
                    questionInfo.set('boardId',re.split('/board/',item['boardLink'])[1])
                    questionInfo.set('pageNum',item['pageNum'])
                    questionInfo.set('questionLink',item['questionLinkList'][index])
                    questionInfo.set('questionType',item['questionTypeList'][index])
                    questionInfo.set('questionName',item['questionNameList'][index])
                    questionInfo.set('questionReleaseDatetime',item['questionReleaseDatetimeList'][index])
                    questionInfo.set('questionAuthorId',item['questionAuthorIdList'][index])
                    questionInfo.set('questionReplyCount',int(item['questionReplyCountList'][index]))
                    #questionInfo.set('questionLastReplyLink',item['questionLastReplyLinkList'][index])
                    questionInfo.set('questionLastReplyDatetime',item['questionLastReplyDatetimeList'][index])
                    #questionInfo.set('questionLastReplyId',item['questionLastReplyIdList'][index])


                    try:
                        questionInfo.save()
                    except LeanCloudError,e:
                        print e
            except LeanCloudError,e:
                print e



        #return item
        DropItem()

