




# import requests
# from lxml import etree
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# response = requests.get("http://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=20&SID=8ELL9ybJviwrevBfk3U&page=1&doc=7", headers = headers)
# htmlElement = etree.HTML(response.text)
# fundingagency = htmlElement.xpath("//table[@class='FR_table_borders']//tr[@class='fr_data_row']/td/text()")
# grantnumber = htmlElement.xpath("//table[@class='FR_table_borders']//tr[@class='fr_data_row']/td/div/text()")
# print(fund1)
# print(fund2)
# all_addresses = htmlElement.xpath("//div[@class='block-record-info']//td[@class='fr_address_row2']/text()")
# print(all_addresses)

'''
import requests
from lxml import etree
response = requests.get("http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=CitedRefList&parentQid=1&parentDoc=3&qid=9&SID=7AMAMvlTJlniPRJUUt9&colName=WOS&page=1")
# print(type(response.text))
#
htmlElement = etree.HTML(response.text)
count = 1
allrefers = htmlElement.xpath("//div[@id='RECORD_1']")
# print(allrefers)
data = []
titlerefer = []
authorrefer = []
journalrefer = []
others = []
while allrefers != []:
    for a in allrefers:
        titles = a.xpath(".//span[@class='reference-title']/value/text()")
        if titles == []:
            # 这里直接跳了，没title基本就没用了
            count += 1
            allrefers = htmlElement.xpath("//div[@id='RECORD_{}']".format(count))
            break
        print(titles)
            # titles = ['not available']
        titlerefer.append(titles)
        authors = a.xpath(".//a[@title='Find more records by this author']//text()")
        authorrefer.append(authors)
        journals = a.xpath(".//div/value/text()")
        journalrefer.append(journals)

        othertitles = a.xpath(".//div/span[@class='label']/text()")
        if 'By: ' in othertitles:

            othertitles.remove('By: ')
        # print(othertitles)
        othercontents = a.xpath(".//div/span[@class='data_bold']/value/text()")
        # print(othercontents)
        other = list(zip(othertitles, othercontents))
        print(other)
        # print(a.xpath(".//a[@title='Find more records by this author']//text()"))
        # b = ''.join(a.xpath(".//a[@title='Find more records by this author']//text()"))
        # print(b)
        # print(a.xpath(".//div/value/text()"))
        data.append(''.join(a.xpath(".//span[@class='label']//text()|.//span[@class='label']//following-sibling::text()")))
        # print(b)
        count += 1

        allrefers = htmlElement.xpath("//div[@id='RECORD_{}']".format(count))
# print(data)
# author = ''.join([s for s in data if "By" in s]).strip().replace("\n", "")
# print(author)
# print(allrefers)
# data = []
# for a in allrefers:
#     print(''.join(a.xpath(".//text()")))
#     data.append(''.join(a.xpath(".//text()")))
# print(data)



# a = ''.join(allrefers).split('\n')
# print(a)

# fund = ''.join(htmlElement.xpath("//table[@class='FR_table_borders']//text()")).strip().replace("\n", "")
# print(fund)
# url2 = htmlElement.xpath("//a[@class='paginationNext snowplow-navigation-nextpage-top']/@href")
# print(url2)
# while '\n' in allrefers:
#     allrefers.remove('\n')

# for refer in allrefers:
#     if refer == '\n'
# print('***'.join(allrefers).replace('\n', '').split('***'))
# print(type(response.content))
# print(allrefers)
# print(response.content.decode('utf-8'))
'''
# import time
# lis = 'Publisher AMER SCIENTIFIC PUBLISHERS, 26650 THE OLD RD, STE 208, VALENCIA, CA 91381-0751 USA'
# s = time.perf_counter()
# lis1 = lis.replace('Publisher ', '', 1)
# print(lis1)
# print(time.perf_counter()-s)
# import re
# s = time.perf_counter()
# strinfo = re.compile(r'Publisher ')
# b = strinfo.sub('', lis)
# print(b)
# print(time.perf_counter()-s)
# s = time.perf_counter()
#
# b = ' '.join(lis.split(' ')[1:])
# print(b)
# print(time.perf_counter()-s)