from selenium import webdriver
import time

driver = webdriver.Chrome('e:/crawler/chromedriver.exe')

driver.get("http://www.naver.com")
time.sleep(3)
search = driver.find_element_by_xpath('//*[@id="query"]')
search.send_keys("교보문고\n")
time.sleep(3)

driver.find_element_by_xpath('//*[@id="main_pack"]/div[2]/ul/')
time.sleep(5)

driver.close()