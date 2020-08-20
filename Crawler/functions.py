import time
import pathlib 
import json
import click
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#mettre le path de votre chromedriver
chrome_path = r"C:\Users\Hamza\Downloads\chromedriver_win32 (1)\chromedriver.exe"

def get_browser(url,usr,pwd,chrome_path=chrome_path):
    driver = webdriver.Chrome(chrome_path)
    driver.get("https://twitter.com/login")
    #driver.implicitly_wait(1)
    time.sleep(1)
    email = driver.find_element_by_name('session[username_or_email]')
    email.send_keys(usr)
    password = driver.find_element_by_name('session[password]')
    password.send_keys(pwd)
    password.send_keys(Keys.ENTER)
    return(driver)
def post_detail(driver):
    """function that takes the id of a twitter post and return data about that post"""
    time.sleep(1)
    li=[]
    try:
        contenu1=driver.find_element_by_xpath(".//div[contains(@class ,'css-901oao r-hkyrab r-1k78y06 r-1blvdjr r-16dba41')]").text
    except:
        contenu1=driver.find_element_by_xpath(".//div[contains(@class ,'css-901oao r-hkyrab r-1qd0xha r-1blvdjr r-16dba41')]").text
    try:
        image=driver.find_element_by_xpath(".//img[@alt='Image']").get_attribute("src")
    except:
        image=""
    date=driver.find_element_by_xpath(".//div[contains(@class ,'css-901oao r-1re7ezh r-1qd0xha')]/span").text
    try:
        nb1=driver.find_elements_by_xpath(".//div[contains(@class ,'css-1dbjc4n r-1gkumvb r-1efd50x')]/div")[0].text
    except:
        nb1=0
    try:
        nb2=driver.find_elements_by_xpath(".//div[contains(@class ,'css-1dbjc4n r-1gkumvb r-1efd50x')]/div")[1].text
    except:
        nb2=0
    i=0
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Show more replies')]"))).click()
    except:
        pass
    users_url=[]
    for i in range(10):
        try:
            a=driver.find_elements_by_xpath(".//article[contains(@class ,'css-1dbjc4n r-1loqt21')]")
            user=a[i].find_element_by_xpath(".//a[contains(@class ,'css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21')]").text
            user_url=a[i].find_element_by_xpath(".//a[contains(@class ,'css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21')]").get_attribute("href")
            users_url.append(user_url)
            try:
                comment=a[i].find_element_by_xpath(".//div[contains(@class ,'css-901oao r-hkyrab r-1k78y06 r-a023e6')]").text
            except:
                comment=a[i].find_element_by_xpath(".//div[contains(@class ,'css-901oao r-hkyrab r-1qd0xha r-a023e6')]").text
            element=a[i].find_element_by_xpath(".//a[contains(@class ,'r-1re7ezh r-1loqt21 ')]")
            driver.execute_script("arguments[0].scrollIntoView();",element)
            date=a[i].find_element_by_xpath(".//a[contains(@class ,'r-1re7ezh r-1loqt21 ')]").get_attribute("title")
            li.append([user,comment,date])
            i=i+1
        except:
            break
    dic={
        "contenu":contenu1,
        "image":image,
        "date":date,
        "Retweets and comments":nb1,
        "likes":nb2,
        "comments":li
    }
    return(dic,users_url)
def save_data(data,name,folder_path):
    """save data in a specific folder path with the name as argument"""
    try:
        pathlib.Path(folder_path+name).mkdir(parents=True, exist_ok=False)
        images=[]
        images.append(data['image'])
        for e in data['posts']:
            images.append(data['posts'][e]['image'])
        i=0
        for e in images:
            try:
                urllib.request.urlretrieve(e,folder_path+name+"/"+str(i) + '.png')
                i=i+1
                print("succ")
            except:
                i=i+1
                print("errr")
        with open(folder_path+name+"\data.json", "a+", encoding="utf8") as json_file:
            json_file.write("\n")
            json.dump(data, json_file, ensure_ascii=False)
    except:
        print("folder already exists")
        pass


