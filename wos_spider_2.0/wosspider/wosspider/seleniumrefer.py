from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scrapy.http.response.html import HtmlResponse
from selenium.webdriver.chrome.options import Options

def Selenium_refer(url):
    referarticles = []
    authorrefer = []
    journalrefer = []
    others = []
    start = time.perf_counter()
    driver = webdriver.Chrome()
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    time.sleep(1)
    end = time.perf_counter()
    print('=' * 30)
    print('外接selenium引用文献连网用时：{}'.format(end - start))
    count_ref = 1
    count = 1
    allrefers = driver.find_element_by_xpath("//div[@id='RECORD_1']")
    # print(allrefers)
    while True:
        # for a in allrefers:
        try:
            titles = allrefers.find_element_by_xpath(".//span[@class='reference-title']/value").text
            # print('='*30)
            # print("标题：")
            # print(titles)
        except:
            # 这里直接跳了，没title基本就没用了
            count += 1
            try:
                allrefers = driver.find_element_by_xpath("//div[@id='RECORD_{}']".format(count))
            except:
                break
            continue
            # titles = ['not available']
        # print(titles)
        referarticles.append(titles)
        try:
            authors = allrefers.find_element_by_xpath(".//a[@title='Find more records by this author']").text
            # print('=' * 30)
            # print("作者：")
            # print(authors)
        except:
            # 这里直接跳了，没title基本就没用了
            count += 1
            try:
                allrefers = driver.find_element_by_xpath("//div[@id='RECORD_{}']".format(count))
            except:
                break
            continue
        authorrefer.append(authors)
        try:
            journals = allrefers.find_element_by_xpath(".//div/value").text
            # print('=' * 30)
            # print("期刊：")
            # print(journals)
            journalrefer.append(journals)
        except:
            journalrefer.append('')
        # 提取其他信息是用了zip粗暴方法，即小概率情况可能出现不匹配情况
        ottitle = []
        try:
            othertitles = allrefers.find_elements_by_xpath(".//div/span[@class='label']")
            for a in othertitles:
                # print(a.text)
                if 'By: ' in a.text:
                    a.text = a.text.replace('By: ', '')
                ottitle.append(a.text)
            # print("其他：")
            # print('=' * 30)
            # print(ottitle)
            otcont = []
            othercontents = allrefers.find_elements_by_xpath(".//div/span[@class='data_bold']/value")
            for i in othercontents:
                # print(i.text)
                otcont.append(i.text)
            # print('=' * 30)

            # print(otcont)
            other = list(zip(ottitle, otcont))
            others.append(other)
        except:
            others.append([])
        count += 1
        try:
            allrefers = driver.find_element_by_xpath("//div[@id='RECORD_{}']".format(count))
        except:
            break
            # 引用超过30篇就会有下一页的问题
    # print(count)
    try:

        while True:
            start = time.perf_counter()
            next = driver.find_element_by_xpath("//a[@class='paginationNext snowplow-navigation-nextpage-top']")
            next.click()

            # driver.implicitly_wait(100)
            WebDriverWait(driver, 100, 0.5).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='RECORD_{}']".format(count))))
            # time.sleep(5)
            count_ref += 1
            end = time.perf_counter()
            print('=' * 30)
            print('外接selenium引用文献翻到第{}页连网用时：{}'.format(count_ref, end - start))

            print(driver.current_url)
            # driver.get(url)

            allrefers = driver.find_element_by_xpath("//div[@id='RECORD_{}']".format(count))
            # print(allrefers)
            while True:
                try:
                    titles = allrefers.find_element_by_xpath(".//span[@class='reference-title']/value").text
                    # print(titles)

                except:
                    # 这里直接跳了，没title基本就没用了
                    count += 1
                    try:
                        allrefers = driver.find_element_by_xpath("//div[@id='RECORD_{}']".format(count))
                    except:
                        break
                    continue
                # print(titles)
                referarticles.append(titles)
                try:
                    authors = allrefers.find_element_by_xpath(".//a[@title='Find more records by this author']").text
                    # print(authors)
                except:
                    # 这里直接跳了，没title基本就没用了
                    count += 1
                    try:
                        allrefers = driver.find_element_by_xpath("//div[@id='RECORD_{}']".format(count))
                    except:
                        break
                    continue
                authorrefer.append(authors)

                try:
                    journals = allrefers.find_element_by_xpath(".//div/value").text
                    # print('=' * 30)
                    # print("期刊：")
                    # print(journals)
                    journalrefer.append(journals)
                except:
                    journalrefer.append('')
                # 提取其他信息是用了zip粗暴方法，即小概率情况可能出现不匹配情况
                ottitle = []
                try:
                    othertitles = allrefers.find_elements_by_xpath(".//div/span[@class='label']")
                    for a in othertitles:
                        # print(a.text)
                        if 'By: ' in a.text:
                            a.text = a.text.replace('By: ', '')
                        ottitle.append(a.text)
                    # print("其他：")
                    # print('=' * 30)
                    # print(ottitle)
                    otcont = []
                    othercontents = allrefers.find_elements_by_xpath(".//div/span[@class='data_bold']/value")
                    for i in othercontents:
                        # print(i.text)
                        otcont.append(i.text)
                    # print('=' * 30)

                    # print(otcont)
                    other = list(zip(ottitle, otcont))
                    others.append(other)
                except:
                    others.append([])
                count += 1
                try:
                    allrefers = driver.find_element_by_xpath("//div[@id='RECORD_{}']".format(count))
                except:
                    break

    except:
        pass
    driver.close()
    print('='*30)
    print('该篇文章引用了：{}篇'.format(len(referarticles)))
    # print(len(referarticles))
    return referarticles, authorrefer, journalrefer, others

# if __name__ == '__main__':
#     url = 'http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=CitedRefList&parentQid=17&parentDoc=15&qid=19&SID=5DMyGYTActOeLsTocvB&colName=WOS&page=1'
#     referarticles, authorrefer, journalrefer, others = Selenium_refer(url)
#     print(referarticles)
#     print(len(referarticles))
#     print(authorrefer)
#     print(journalrefer)
#     print(others)
