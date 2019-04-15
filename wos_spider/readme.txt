#说明：
1.网页解析：
web of science 网页分布规则有点奇怪，一般网页会在?query="climate"上变化，但是从下面测试用概览页URL看只有"qid=1"这里变化了，很可能是用户搜索一次产生一个qid，
类似cookie。测试时我清除过cookie，但依然能打开到原网页，于是乎忽视这点能爬就行了

2.爬虫环境
scrapy--crawlspider
随机请求头用了10个
没有用代理IP池
爬虫休眠0.5s（说不定不用休眠也行）



#测试用概览页URL（四次 分别搜索的是climate、energy、climate change、environment）
http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=1&SID=5EpTgjfkjTrGh8RQwsR&&update_back2search_link_param=yes&page=2
http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=1&SID=5EpTgjfkjTrGh8RQwsR&&update_back2search_link_param=yes&page=1
http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=3&SID=5EpTgjfkjTrGh8RQwsR&&update_back2search_link_param=yes&page=2
http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=4&SID=5EpTgjfkjTrGh8RQwsR&&update_back2search_link_param=yes&page=2

#测试用详情页URL
https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=3&SID=5EpTgjfkjTrGh8RQwsR&page=3&doc=22
https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=3&SID=5EpTgjfkjTrGh8RQwsR&excludeEventConfig=ExcludeIfFromFullRecPage&page=3&doc=24&cacheurlFromRightClick=no
https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=3&SID=5EpTgjfkjTrGh8RQwsR&page=1&doc=3