from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from scrapy.http.response.html import HtmlResponse
from selenium.webdriver.chrome.options import Options

def Selenium_article_url(art):
    # def __init__(self):
    url = ''
    driver = webdriver.Chrome()
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('http://apps.webofknowledge.com')
    WebDriverWait(driver, 100, 0.5).until(
        EC.presence_of_element_located((By.XPATH, "//div")))
    # time.sleep(2)
    try:
        input1 = driver.find_element_by_xpath("//div[@class='search-criteria-input-wr']/input")
        input1.send_keys(art)

    except:
        pass
    time.sleep(0.3)
    try:
        # [position()<3]

        selector = driver.find_element_by_xpath("//span[@class='selection']/span[@class='select2-selection select2-selection--single']//span[@id='select2-select1-container']")
        selector.click()
        time.sleep(0.3)
        selector2 = driver.find_element_by_xpath("//input[@class='select2-search__field']")
        # selector2.send_keys('Title') # 打开WOS是英文就用这个
        selector2.send_keys('标题') # 打开WOS是中文的就用它

        time.sleep(0.3)
        selector2.send_keys(Keys.ENTER)


    except:
        pass

    time.sleep(0.3)
    try:
        button = driver.find_element_by_xpath("//button[@class='large-button primary-button margin-left-10']")
        button.click()

    except:
        pass
    # time.sleep(1)
    WebDriverWait(driver, 30, 0.5).until(
        EC.presence_of_element_located((By.XPATH, "//div")))
    try:
        print('=' * 30)
        print(driver.current_url)
        # # 方法一：
        # button2 = driver.find_element_by_xpath("//div[@class='search-results-content']//a/value")
        # button2.click()
        # time.sleep(10)
        # url = driver.current_url
        # print('=' * 30)
        # print(url)

        #方法二：
        urls_pre = driver.find_element_by_xpath("//div[@class='search-results-content']//a[@class='smallV110 snowplow-full-record']")
        url = urls_pre.get_attribute("href")
        print("方法二")
        print('=' * 30)
        print(url)
        # for a in impact:
        #     print(a)
        #     print('*'*30)
        #     print(type(a))

        # print(impact)
        # print(type(impact))
    except:
        print("本文WOS上没有：", art)



    # url = driver.current_url
    # print('=' * 30)
    # print(url)
    response = HtmlResponse(url=url, body=driver.page_source, encoding='utf-8')
    driver.close()
    # source = driver.page_source

    return url, response

if __name__ == '__main__':
    art = 'Geomorphology of the Upper General River Basin, Costa Rica'
    Selenium_article_url(art)