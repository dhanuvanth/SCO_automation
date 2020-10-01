from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r'C:\Users\Dhanu\Downloads\chromedriver.exe')  # check this path
driver.maximize_window()
driver.get('https://www.usalistingdirectory.com/submit.php')

link = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/input')
link.click()
sleep(2)

title = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/input')
title.send_keys('Corporate Training')
sleep(2)

url = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/input')
url.send_keys('https://www.mazenetsolution.com/corporate-training/')
sleep(2)

desc = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/textarea')
desc.send_keys('Corporate Training - - Mazenet is a workforce development organization in Information Technology benefiting many corporates across different geographies')
sleep(2)

keyword = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[6]/td[2]/input')
keyword.send_keys('Corporate Training')
sleep(2)

desc_meta = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[7]/td[2]/textarea')
desc_meta.send_keys('Corporate Training - - Mazenet is a workforce development organization in Information Technology benefiting many corporates across different geographies')
sleep(2)

name = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[8]/td[2]/input')
name.send_keys('Mazenet Solution')
sleep(2)

email = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[9]/td[2]/input')
email.send_keys('mazenetsubmission@gmail.com')
sleep(2)

catageries = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[10]/td[2]/select/option[54]')
catageries.click()
sleep(2)

agree = driver.find_element_by_xpath('//*[@id="AGREERULES"]')
agree.click()
sleep(2)

submit = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[13]/td/input')
submit.click()
sleep(2)