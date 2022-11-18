import os
from os import getcwd,path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#chrome driver 
ch_dir=os.path.join(os.getcwd(),"chromedriver.exe")

class Chrome_driver:
    def __init__(self,dir:str=ch_dir ) -> None:
        self.driver=webdriver.Chrome(executable_path=ch_dir)


  

#driver.get("http://www.project-lara.online")
#driver.find_element(By.XPATH, '//*[@id="navbarToggle"]/div[2]/a[1]').click()

#print(driver.title)
#print(driver.current_url)

#driver.get("http://www.project-lara.online/login")
#driver.implicitly_wait(3)
#driver.find_element(By.ID, 'email').send_keys("david@gmail.com")
#driver.find_element(By.ID, 'password').send_keys("1234")
#driver.find_element(By.XPATH, '//*[@id="submit"]').click()
#driver.implicitly_wait(7)
#xpath  //tagname[@attribute='value']
#driver.find_element(By.XPATH, '/html/body/main/div/div/button').click()
