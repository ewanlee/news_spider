# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import io

class Save2FilePipeline(object):
    def process_item(self, item, spider):
        file_path = './news/' + item['title']
        with io.open(file_path, 'w') as f:
            f.write(item['content'])
