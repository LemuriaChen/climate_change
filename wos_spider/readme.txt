#说明：
0.使用说明：
第一步：web of science上搜索想要的名词如："climate change"
第二步：点击下一页，复制链接，将链接中page=2修改为page=1
第三步：将wosspider.py中start_url那里替换成第二步的链接
第四步：找到第三步链接中的qid后面的数字，将wosspider.py中两个Rule(LinkExtractor())中qid后面数字修改成第三步链接中的qid后面的数字

1.网页解析：
web of science 网页分布规则有点奇怪，一般网页会在?query="climate"上变化，但是从下面测试用概览页URL看只有"qid=1"这里变化了，很可能是用户搜索一次产生一个qid，
类似cookie。测试时我清除过cookie，但依然能打开到原网页，于是乎忽视这点能爬就行了
**********注意：关机会受到影响会找不到原网页*************
经过不断测试，qid=1就是关机后当天的第一次搜索请求

2.爬虫环境
scrapy--crawlspider
（用scrapy shell连接web of science网页会显示400，scrapy自己连会先301再200，用requests库请求连接直接200）
随机请求头用了10个
没有用代理IP池
爬虫休眠0.5s（说不定不用休眠也行）

3.scrapy框架
==========================
item:

title文章标题,
author作者（正好web of science上有全名和缩写全拿下来了）,
abstract摘要（这里摘要background、conclusion这些都会出现，每篇文章不同）
下面两个是关键词
authorkeywords
keywordsplus 
researchareas （作者研究领域）
woscategories（web of science分类）
lang（文章的语言）
issn
refer（引用别人次数）
cited（被引次数）
url（该文章的url）

=============================
middlewares

主要是随机请求头设计
=============================
pipeline

mysql数据库存储
==============================
wosspider

由于web of science在item中内容出现顺序不固定，因此也只能通过字符串子串[s for s in data if "By" in s]遍历方式了

=================================

#测试用概览页URL（四次 分别搜索的是climate、energy、climate change、environment）
http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=1&SID=5EpTgjfkjTrGh8RQwsR&&update_back2search_link_param=yes&page=2
http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=1&SID=5EpTgjfkjTrGh8RQwsR&&update_back2search_link_param=yes&page=1
http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=3&SID=5EpTgjfkjTrGh8RQwsR&&update_back2search_link_param=yes&page=2
http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=4&SID=5EpTgjfkjTrGh8RQwsR&&update_back2search_link_param=yes&page=2

#测试用详情页URL
https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=3&SID=5EpTgjfkjTrGh8RQwsR&page=3&doc=22
https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=3&SID=5EpTgjfkjTrGh8RQwsR&excludeEventConfig=ExcludeIfFromFullRecPage&page=3&doc=24&cacheurlFromRightClick=no
https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=3&SID=5EpTgjfkjTrGh8RQwsR&page=1&doc=3

=======================================
第二天关机测试结果：

#测试用概览页URL
https://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=1&SID=6CzSu6KLF7PERftEXhM&&update_back2search_link_param=yes&page=2

#测试用详情页URL
https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=1&SID=6CzSu6KLF7PERftEXhM&page=2&doc=12
