import os
from os import getcwd,path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#chrome driver 
service_obj=Service(os.path.join(os.getcwd(),"chromedriver.exe"))

#driver
driver=webdriver.Chrome(service=service_obj)

driver.get("http://www.project-lara.online")
print(driver.title)
print(driver.current_url)
driver.implicitly_wait(3.0)
driver.close()