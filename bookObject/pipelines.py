# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json,io

class BookobjectPipeline(object):
    def __init__(self):
        self.fp = io.open('url_name.json','w',encoding='utf-8')
    def process_item(self, item, spider):
        urlitem  = dict(item)
        print(urlitem)
        # s = urlitem['url_name']+'\n'
        #
        # string = json.dumps(s,ensure_ascii=False)
        # print(string)
        # self.fp.write(string)
        return item
    def close_spider(self,spider):
        self.fp.close()
