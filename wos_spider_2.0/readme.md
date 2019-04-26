<div align="left">
    <img src='https://github.com/HUANGZHIHAO1994/storeage/blob/master/images/IMG_1869.jpg?raw=true' height="50" width="50" >
 </div>

## 0.使用说明：（使用步骤）

1. web of science上搜索想要的名词如："climate change"
2. 点击下一页，复制链接，将链接中page=2修改为page=1



![使用说明1](https://github.com/HUANGZHIHAO1994/storeage/blob/master/images/1.gif?raw=true)



3. 将wosspider.py中start_url那里替换成第二步的链接`

   ```python
   start_urls = ['http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=3&SID=5EpTgjfkjTrGh8RQwsR&&update_back2search_link_param=yes&page=1']
   ```

   

4. 找到第三步链接中的qid后面的数字，将wosspider.py中两个Rule(LinkExtractor())中qid后面数字修改成第三步链接中的qid后面的数字`

   ```python
   rules = (
           Rule(LinkExtractor(allow=r'.+summary.do\?.+&qid=3.+&page=\d'),follow=True),
           Rule(LinkExtractor(allow=r'.+full_record.do\?.+&qid=3.+&page=\d&doc=\d'), callback="parse_item", follow=True)
       )
   ```

   

## 1.网页解析：(解析看gif)

- web of science 网页分布规则有点奇怪，一般网页会在?query="climate"上变化，但是从下面测试用概览页URL看只有"qid=1"这里变化了，很可能是用户搜索一次产生一个qid，
  类似cookie。测试时我清除过cookie，但依然能打开到原网页，于是乎忽视这点能爬就行了。
- **注意：关机会受到影响会找不到原网页**
- 最终，经过不断测试，qid=1就是关机后当天的第一次搜索请求



1. 文章 *title* 信息

```python
 title = ''.join(htmlElement.xpath("//div[@aria-label='Main content']//div[@class='title']//text()"))
```



## ![title](https://github.com/HUANGZHIHAO1994/storeage/blob/master/images/2.gif?raw=true)

2.  文章其余信息

```python
alls = htmlElement.xpath("//div[@class='block-record-info']/p[@class='FR_field']")
```

```python
author = ''.join([s for s in data if "By" in s]).strip().replace("\n", "")
        abstract = ''.join(data[1]).strip().replace("\n", "")
        authorkeywords = ''.join([s for s in data if "Author Keywords" in s]).strip().replace("\n", "")
        keywordsplus = ''.join([s for s in data if "KeyWords Plus" in s]).strip().replace("\n", "")
        researchareas = ''.join([s for s in data if "Research Areas" in s]).strip().replace("\n", "")
        woscategories = ''.join([s for s in data if "Web of Science Categories" in s]).strip().replace("\n", "")
        lang = ''.join([s for s in data if "Language" in s]).strip().replace("\n", "")
        issn = ''.join([s for s in data if "ISSN" in s]).strip().replace("\n", "")
        refer = ''.join([s for s in data if "Cited References in Web of Science Core Collection" in s]).strip().replace("\n", "")
        cited = ''.join([s for s in data if "Times Cited in Web of Science Core Collection" in s]).strip().replace("\n", "")
        url = response.url
```

![else](https://github.com/HUANGZHIHAO1994/storeage/blob/master/images/3.gif?raw=true)

## 2.爬虫环境
- scrapy--crawlspider
  （用scrapy shell连接web of science网页会显示400，scrapy自己连会先301再200，用requests库请求连接直接200）

- 随机请求头用了10个

- 没有用代理IP池

- 爬虫休眠0.5s（说不定不用休眠也行）

  

## 3.scrapy框架

1. **item:**

   ```python
   class WosspiderItem(scrapy.Item):
   
   '''
   说明：
   
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
   '''
   ```

2. **middlewares**

   主要是随机请求头设置

   ```python
   class UserAgentDownloadMiddleware(object):
   ```

3. **pipeline**

   mysql数据库存储

4. **wosspider**

   由于web of science在item中内容出现顺序不固定，因此也只能通过字符串子串[s for s in data if "By" in s]遍历方式了

## 4. 测试用url

测试用概览页URL（四次 分别搜索的是climate、energy、climate change、environment）

1. http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=1&SID=5EpTgjfkjTrGh8RQwsR&&update_back2search_link_param=yes&page=2
2. http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=1&SID=5EpTgjfkjTrGh8RQwsR&&update_back2search_link_param=yes&page=1
3. http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=3&SID=5EpTgjfkjTrGh8RQwsR&&update_back2search_link_param=yes&page=2
4. http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=4&SID=5EpTgjfkjTrGh8RQwsR&&update_back2search_link_param=yes&page=2







测试用详情页URL

1. https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=3&SID=5EpTgjfkjTrGh8RQwsR&page=3&doc=22
2. https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=3&SID=5EpTgjfkjTrGh8RQwsR&excludeEventConfig=ExcludeIfFromFullRecPage&page=3&doc=24&cacheurlFromRightClick=no
3. https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=3&SID=5EpTgjfkjTrGh8RQwsR&page=1&doc=3

===================

第二天关机测试结果：

测试用概览页URL

1. https://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=GeneralSearch&parentQid=&qid=1&SID=6CzSu6KLF7PERftEXhM&&update_back2search_link_param=yes&page=2

测试用详情页URL

1. https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=1&SID=6CzSu6KLF7PERftEXhM&page=2&doc=12
