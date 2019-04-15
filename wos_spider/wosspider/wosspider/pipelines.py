# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from pymysql import cursors

class WosspiderPipeline(object):
    def __init__(self):
        dbparams = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '1234',
            'database': 'wos',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['title'], item['author'], item['abstract'], item['authorkeywords'], item['keywordsplus'], item['researchareas'],
        item['woscategories'], item['lang'], item['issn'], item['refer'], item['cited'], item['url']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into article(id,title,author,abstract,authorkeywords,keywordsplus,researchareas,woscategories,lang,issn,refer,cited,url) values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql