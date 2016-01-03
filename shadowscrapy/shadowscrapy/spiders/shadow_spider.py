# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from shadowscrapy.items import ShadowscrapyItem


class shadowSpider(Spider):
    name = "shadow"
    allowed_domains = ["feixunvpn.org"]
    TESTSS_URL = "http://www.feixunvpn.com/page/testss.html"
    start_urls = [TESTSS_URL]

    def parse(self, response):
        sel = Selector(response)
        proxylist = sel.xpath('//div[@class="pagecontent"]/div[@class="testvpnitem"]')

        had_target_ip = False
        for p in proxylist:
            item = ShadowscrapyItem()
            srv_name = p.xpath('b/text()').extract()[0]
            item["server"] = p.xpath('span[1]/text()').extract()[0]
            port = int(p.xpath('text()').extract()[2].replace(u'端口：', u'').strip())
            item["server_port"] = port
            item["password"] = p.xpath('text()').extract()[3].replace(u'密码：', u'').strip()
            item["method"] = p.xpath('span[2]/text()').extract()[0]

            item["local_port"] = 1080
            item["timeout"] = 60

            if u'美国' in srv_name:
                had_target_ip = True
                yield item

        if not had_target_ip:
            yield Request(self.TESTSS_URL, callback=self.parse)
