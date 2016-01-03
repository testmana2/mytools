# -*- coding: utf-8 -*-

# Scrapy settings for shadowscrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'shadowscrapy'

SPIDER_MODULES = ['shadowscrapy.spiders']
NEWSPIDER_MODULE = 'shadowscrapy.spiders'

# ITEM_PIPELINES = {
#     'shadowscrapy.pipelines.ShadowscrapyPipeline': 800,
# }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1"

COOKIES_ENABLES = False
DOWNLOAD_DELAY = 3
