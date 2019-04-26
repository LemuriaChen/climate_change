# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
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
        self.cursor2 = self.conn.cursor()
        self.cursor3 = self.conn.cursor()
        self._sql = None
        self._sql2 = None
        self._sql3 = None

    def process_item(self, item, spider):
        start = time.perf_counter()
        try:

            # 查重处理
            self.cursor.execute(
                """select * from articles where wosnum = %s""",
                item['wosnum'])
            # 是否有重复数据
            repetition = self.cursor.fetchone()

            # wosnum 有些文章没有，增加doi判断
            self.cursor.execute(
                """select * from articles where doi = %s""",
                item['doi'])
            # 是否有重复数据
            repetition2 = self.cursor.fetchone()
            # 重复
            if repetition and repetition2:
                pass
            else:


                self.cursor.execute(self.sql, (
                item['wosnum'], item['title'], item['author'], item['author2'], item['reprintauthor'], item['journal'],
                item['volume'], item['issue'], item['page'], item['doi'], item['pubdate'], item['documenttype'],
                item['publisher'], item['researchdomain'], item['abstract'], item['authorkeywords'],
                item['keywordsplus'], item['reprintaddress'], item['address'], item['emailaddress'], item['fund'],
                item['researchareas'], item['woscategories'], item['lang'], item['issn'], item['eissn'], item['idsnum'],
                item['refer'], item['cited'], item['url'], item['referarticles'], item['authorrefer'],
                item['journalrefer'], item['othersrefer'], item['coauthors'], item['authorlistkey'],item['impact'],item['authorid']))
                print('=' * 30)
                print('主表')
                self.conn.commit()


                # # 引用表
                # for i in range(len(eval(item['referarticles']))):
                #     citedtitles = eval(item['referarticles'])[i][0]
                #     citedauthors = eval(item['authorrefer'])[i][0]
                #     citedjournals = eval(item['journalrefer'])[i][0]
                #     citedothers = eval(item['othersrefer'])[i][0]
                #     self.cursor2.execute(
                #         """insert into refer(id, citedtitles, citedauthors, citedjournals ,citedothers, wosnum, doi, title, author, refer)
                #         value (null,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                #         (citedtitles,
                #          citedauthors,
                #          citedjournals,
                #          citedothers,
                #          item['wosnum'],
                #          item['doi'],
                #          item['title'],
                #          item['author'],
                #          item['refer']))
                #     self.conn.commit()
                #
                #     # 作者表
                # self.cursor3.execute("""insert into author(id, wosnum, authorlistkey,title,doi, address, emailaddress ,pubdate, researchareas,woscategories, lang)
                #         value (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (item['wosnum'],
                #              item['authorlistkey'],
                #              item['title'],
                #              item['doi'],
                #              item['address'],
                #              item['emailaddress'],
                #              item['pubdate'],
                #              item['researchareas'],
                #              item['woscategories'],
                #              item['lang']))
                # print('=' * 30)
                # print('作者表')
                # self.conn.commit()

        except Exception as error:
                # 出现错误时打印错误日志
                print(error)
        end = time.perf_counter()
        print('=' * 30)
        print('存入数据库用时：{}'.format(end - start))
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                    insert into articles1(id,wosnum,title,author,author2,reprintauthor,journal,volume,issue,page,doi, pubdate,documenttype,publisher,researchdomain,abstract,authorkeywords,keywordsplus,reprintaddress,address,emailaddress,fund,researchareas,woscategories,lang,issn,eissn,idsnum,refer,cited,url,referarticles,authorrefer,journalrefer,othersrefer,coauthors,authorlistkey,impact,authorid) values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                """
            return self._sql
        return self._sql

            # self._sql = """
                #             insert into articles(id,wosnum,title,author,author2,reprintauthor,journal,volume,issue,page,doi, pubdate,documenttype,publisher,researchdomain,abstract,authorkeywords,keywordsplus,reprintaddress,address,emailaddress,fund,researchareas,woscategories,lang,issn,eissn,idsnum,refer,cited,url,referarticles,authorrefer,journalrefer,othersrefer,coauthors,authorlistkey) values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                #             """


'''
                # 引用表
                for i in range(len(eval(item['referarticles']))):
                    citedtitles = eval(item['referarticles'])[i][0]
                    citedauthors = eval(item['authorrefer'])[i][0]
                    citedjournals = eval(item['journalrefer'])[i][0]
                    citedothers = eval(item['othersrefer'])[i][0]

                    self.cursor2.execute(self.sql2, (citedtitles,
                         citedauthors,
                         citedjournals,
                         citedothers,
                         item['wosnum'],
                         item['doi'],
                         item['title'],
                         item['author'],
                         item['refer']))
                    self.conn.commit()
                    

                # 作者表
                    self.cursor3.execute(self.sql3, (item['wosnum'],
                         item['authorlistkey'],
                         item['title'],
                         item['doi'],
                         item['address'],
                         item['emailaddress'],
                         item['pubdate'],
                         item['researchareas'],
                         item['woscategories'],
                         item['lang']))
                    print('=' * 30)
                    print('作者表')
                    self.conn.commit()

                    # self.cursor3.execute(
                    #     """insert into author(id, wosnum, authorlistkey,title,doi, address, emailaddress ,pubdate, researchareas,woscategories, lang)
                    #     value (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    #     (item['wosnum'],
                    #      item['authorlistkey'],
                    #      item['title'],
                    #      item['doi'],
                    #      item['address'],
                    #      item['emailaddress'],
                    #      item['pubdate'],
                    #      item['researchareas'],
                    #      item['woscategories'],
                    #      item['lang']))
                    self.conn.commit()




        except Exception as error:
            # 出现错误时打印错误日志
            print(error)

        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                insert into articles(id,wosnum,title,author,author2,reprintauthor,journal,volume,issue,page,doi, pubdate,documenttype,publisher,researchdomain,abstract,authorkeywords,keywordsplus,reprintaddress,address,emailaddress,fund,researchareas,woscategories,lang,issn,eissn,idsnum,refer,cited,url,referarticles,authorrefer,journalrefer,othersrefer,coauthors,authorlistkey) values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """
            return self._sql
        return self._sql

    @property
    def sql2(self):
        if not self._sql2:
            self._sql2 = """insert into refer(id, citedtitles, citedauthors, citedjournals ,citedothers, wosnum, doi, title, author, refer)
                        value (null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            return self._sql2
        return self._sql2

    @property
    def sql3(self):
        if not self._sql3:
            self._sql3 = """insert into author(id, wosnum, authorlistkey,title,doi, address, emailaddress ,pubdate, researchareas,woscategories, lang)
                        value (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            return self._sql3
        return self._sql3
'''