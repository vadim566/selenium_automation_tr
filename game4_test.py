import os
from os import getcwd,path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from chrome_drive import ch_dir

def drive_init(url):
    driver=webdriver.Chrome(executable_path=ch_dir)
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(3)
    
    total_tests=5
    tests=0
    for i in range(total_tests):
        tests=tests+check_test1(driver)

    print(u"tests succeeded "+str(tests)+ " / "+str(total_tests))

def check_test1(driver)->tuple:
    right_answer=driver.find_element(By.XPATH,'//*[@id="ans"]').get_attribute("value")

    select_answer=driver.find_element(By.XPATH,"//input[@value='"+right_answer+"']")
    #print(right_answer)
    #print(select_answer.text)
    driver.implicitly_wait(10)
    try:
        select_answer.click()
    except:
        print("click handled ")
    try:
        select_answer.click()
    except:
        print("click handled ")


    driver.implicitly_wait(3)

    resp_answer=driver.find_element(By.CLASS_NAME ,"alert").text
    #print(resp_answer)

    good_text='Right answer you got 1 point'
    if(good_text==resp_answer):
        print("test passed")
        return 1
    else:
        return 0


if __name__=="__main__":
    game4_list=["https://www.project-lara.online/game4/['alice_in_wonderland',0,0]?alice_in_wonderlandgame+4+new=",\
       "https://www.project-lara.online/game4/['mangiri',0,0]?mangirigame+4+new=",\
        "https://www.project-lara.online/game4/['barngarla_songs',0,0]?barngarla_songsgame+4+new=" ]
    for url in game4_list:
        drive_init(url)