from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scrapy.http.response.html import HtmlResponse
from selenium.webdriver.chrome.options import Options

def Selenium_impact_id(url):
    # def __init__(self):
    driver = webdriver.Chrome()
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 100, 0.5).until(
        EC.presence_of_element_located((By.XPATH, "//div")))
    # time.sleep(2)
    try:
        researcherid = driver.find_element_by_xpath("//a[@class='snowplow-view-ResearcherID-and-ORCID']")
        researcherid.click()

    except:
        pass
    time.sleep(1)
    try:
        # [position()<3]
        authorid = driver.find_element_by_xpath("//span[@style='display: inline;']/table[@class='FR_table_borders']").text.strip()
        # for a in authorid:
        #     print(a)
        #     print('*'*30)
        #     print(type(a))
        print('=' * 30)
        print(authorid)
        print(type(authorid))
    except:
        print("本文没有1")
        print(driver.current_url)
        authorid = ''
    time.sleep(1)
    try:
        impact1 = driver.find_element_by_xpath("//a[@class='focusable-link snowplow-JCRoverlay']")
        impact1.click()

    except:
        pass
    time.sleep(1)
    try:
        impact = driver.find_element_by_xpath("//div[@class='overlayJCRblock']").text.strip()
        # for a in impact:
        #     print(a)
        #     print('*'*30)
        #     print(type(a))
        print('=' * 30)
        print(impact)
        print(type(impact))
    except:
        print("本文没有2")
        impact = ''

    # try:
    #     impact = driver.find_element_by_xpath("//div[@class='overlayJCRblock']//text()").get()
    #     print('=' * 30)
    #     print(impact)
    #     print(type(impact))
    # except:
    #     print("本文没有")
    #     impact = ''
    time.sleep(1)


    driver.close()
    # source = driver.page_source
    # response = HtmlResponse(url=driver.current_url, body=source, request=request, encoding='utf-8')

    return impact, authorid

