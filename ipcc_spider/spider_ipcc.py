from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request
import requests
import threading
import os
import datetime
import time


class MySpider:

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}

    pdfPath = "./"

    def startUp(self, url):

    # Initializing Chrome browser
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)


        # Initializing variables
        self.threads = []
        self.No = 0
        self.pdfNo = 0



        try:
            if not os.path.exists(MySpider.pdfPath):
                os.mkdir(MySpider.pdfPath)
            # pdfs = os.listdir(MySpider.pdfPath)
            # for pdf in pdfs:
            #     s = os.path.join(MySpider.pdfPath, pdf)
            #     os.remove(s)
        except Exception as err:
            print(err)

        self.driver.get(url)



    def closeUp(self):
        try:
            self.driver.close()
            # print(self.pdfNo)

        except Exception as err:
            print(err)


    def download(self, data, mFile):
        try:
            if data:
                # fobj = open(MySpider.pdfPath + "\\" + mFile, "wb")
                r = requests.get(data, stream=True)

                with open(MySpider.pdfPath + "\\" + mFile, "wb") as pdf:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            pdf.write(chunk)

                # r = requests.get(data)
                # fobj.write(r.content)

                self.pdfNo += 1
                # fobj.close()
                # print("download ", mFile)
        except:
            pass


    def processSpider(self):
        try:
            # time.sleep(1)
            a_s = self.driver.find_elements_by_xpath("//div[@class='section-content']//a")
            for a in a_s:


                try:
                    href = a.get_attribute('href')
                    p = href.rfind("/")
                    mFile = no + href[p+1:]

                except:
                    href = ""

                self.No = self.No + 1
                no = str(self.No)
                while len(no) < 3:
                    no = "0" + no
                print(no)

                if href:
                    thr = threading.Thread(target=self.download, args=(href, mFile))
                    thr.setDaemon(False)
                    thr.start()
                    self.threads.append(thr)

                else:
                    mFile = ""



        except Exception as err:
            print(err)


    def executeSpider(self, url):
        starttime = datetime.datetime.now()
        print("Spider starting......")
        self.startUp(url)
        self.processSpider()
        self.closeUp()
        for t in self.threads:
            t.join()
        print("Spider completed......")
        endtime = datetime.datetime.now()
        elapsed = (endtime - starttime).seconds
        print("Total ", elapsed, " seconds elapsed")

start = time.perf_counter()
count = 1
for x in range(1, 6):
    for y in range(1, 4):
        print('爬到第{}/15个'.format(count))
        count += 1
        pdfPath = '{}{}'.format(x, y)
        os.mkdir(pdfPath)
        os.chdir(pdfPath)
        url = 'https://www.ipcc.ch/report/ar{}/wg{}/'.format(x, y)
        spider = MySpider()
        spider.executeSpider(url)
times = time.perf_counter() - start
print("总耗时:{}".format(times))
        # else:
        #     d = os.path.dirname(__file__)
        #     parent_path = os.path.dirname(d)
        #     os.chdir(parent_path)
        #     pdfPath = 'download_ar{}_wg{}'.format(x, y)
        #     os.mkdir(pdfPath)
        #     os.chdir(pdfPath)
        #     url = 'https://www.ipcc.ch/report/ar{}/wg{}/'.format(x, y)
        #     spider = MySpider()
        #     spider.executeSpider(url)
        #     count += 1


