from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome('e:/crawler/chromedriver.exe')

driver.get("http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79")
time.sleep(3)

source = driver.page_source
s1 = BeautifulSoup(source,"html.parser")
s2 = s1.find_all("div", class_="title")
for data in s2[4:]:
    print(data.text.strip())
s3 = s1.find_all("div", class_="author")
for data in s3:
    print(data.text.strip().replace("\t", ""))
s4 = s1.find_all("div", class_="price")
for data in s4:
    print(data.text.strip())
time.sleep(5)
driver.close()