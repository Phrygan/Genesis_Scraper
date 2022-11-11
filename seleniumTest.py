import os 
import time

from selenium import webdriver
import requests

PATH = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')
driver = webdriver.Chrome(PATH)

url = "https://students.livingston.org/livingston"
driver.get(url)

user_info = []
with open("credentials.txt", "rt") as credentials:
    for line in credentials:
        user_info.append(line[0:-1])
        
username = user_info[0]
password = user_info[1]

driver.find_element_by_id("j_username").send_keys(username)
driver.find_element_by_id("j_password").send_keys(password)
driver.find_element_by_class_name("saveButton").click()

classgrades = []
for x in range(2, 11):
    try:
        classgrades.append(driver.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[%s]/td[3]/table/tbody/tr/td[1]" % x).text)
    except:
        print("Exception Occured");
print(classgrades)
time.sleep(1)


driver.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[1]").click()
print(driver.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/div/table/tbody/tr[3]/td[6]").text)
time.sleep(1)

driver.quit()
