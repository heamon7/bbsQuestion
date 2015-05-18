# -*- coding: utf-8 -*-

# Scrapy settings for bbsQuestion project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bbsQuestion'

SPIDER_MODULES = ['bbsQuestion.spiders']
NEWSPIDER_MODULE = 'bbsQuestion.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bbsQuestion (+http://www.yourdomain.com)'
LOG_LEVEL = 'INFO'
DOWNLOAD_TIMEOUT = 700

CONCURRENT_REQUESTS = 70
CONCURRENT_REQUESTS_PER_DOMAIN = 70

APP_ID_S = 'w359bnk9hh7z8fx0hsy6ee7b2tmf5va250hstatnu0a2iqbi'
MASTER_KEY_S = '6k2z44pax0ueopc4qmbnxa8gzg6inon0t2a7d1fc6czqm1ei'

APP_ID = 'th0crrtntqpr8o7742r2q6q4i8b0lsmmgnzdhe6xw3e4lyze'
MASTER_KEY = '3edds3mshfwrg78vphspyqi21mnkau15yjpthpq03yst708e'

ITEM_PIPELINES = {
    'bbsQuestion.pipelines.QuestionPipeline': 300,
   # 'zhihut.pipelines.SecondPipline': 800,
}

DEFAULT_REQUEST_HEADERS = {
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2',
           'Connection': 'keep-alive',
           'Host': 'bbs.byr.cn',
           'Referer': 'http://bbs.byr.cn/',
           'X-Requested-With': 'XMLHttpRequest'
}

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'

AJAXCRAWL_ENABLED = True