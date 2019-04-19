from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.request
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
url = 'https://www.ipcc.ch/report/ar1/wg1/'
driver.get(url)
# time.sleep(1)
a_s = driver.find_elements_by_xpath("//div[@class='section-content']//a")
# for a in a_s:
#     print(a.text)
html=driver.page_source
soup=BeautifulSoup(html,"lxml")
print(soup.find("div",attrs={'class':'section-content'}))
# print(soup)

