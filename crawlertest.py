from selenium import import webdriver
import time

driver = webdriver.Chrome('e:/crawler/chromedriver.exe')

driver.get("http://www.naver.com")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="account"]/div/a/i').click()

time.sleep(3)
userid = driver.find_element_by_xpath('//*[@id="id"]')
userid.send_keys('abc1234')
userpw = driver.find_element_by_xpath('//*[@id="pw"]')
userpw.send_keys('abc1234')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/a/i').click()
time.sleep(5)

driver.close()