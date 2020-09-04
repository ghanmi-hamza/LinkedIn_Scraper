import time
import pathlib 
import json
import click
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from abc import ABC
class Driver(ABC):

    def get_user_info(self,driver,url):
        pass
    
    def get_publications(self,user_id,n,comments):
        pass
    
    def get_comment_by_publication(self,publication_id):
        pass


class TwitterDriver(Driver):
    def __init__(self,driver=''):
        self.driver=driver
        """Constructeur de notre classe"""
        pass
    def get_browser(self,usr,pwd):
        options = webdriver.firefox.options.Options()
        options.headless = True
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\Hamza\Downloads\geckodriver.exe", options=options)
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        email = self.driver.find_element_by_name('session[username_or_email]')
        email.send_keys(usr)
        password = self.driver.find_element_by_name('session[password]')
        password.send_keys(pwd)
        password.send_keys(Keys.ENTER)
   
        
    def get_user_info(self,user_id):
        """function that takes the url of the user and return some info about it"""
        self.driver.get("https://twitter.com/"+str(user_id))
        time.sleep(3)
        #c=self.driver.find_element_by_xpath(".//div[@class='css-1dbjc4n r-1habvwh']").text
        name=self.driver.find_element_by_xpath(".//div[@class='css-901oao r-hkyrab r-1qd0xha r-1b6yd1w r-1vr29t4 r-ad9z0x r-bcqeeo r-qvutc0']").text
        #name=c.split("\n")[0]
        nb_tweets=self.driver.find_element_by_xpath(".//div[@class='css-901oao css-bfa6kz r-1re7ezh r-1qd0xha r-n6v787 r-16dba41 r-1sf4r6n r-bcqeeo r-qvutc0']").text
        #nb_tweets=c.split("\n")[1]
        #tagName=self.driver.find_element_by_xpath(".//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0']").text
        #tagName=self.driver.find_element_by_xpath(".//div[@class='css-1dbjc4n r-18u37iz r-1wbh5a2']").text
        UserDescription=self.driver.find_element_by_xpath(".//div[@data-testid='UserDescription']").text
        data=self.driver.find_element_by_xpath(".//div[@data-testid='UserProfileHeader_Items']").text
        ss=self.driver.find_elements_by_xpath(".//div[@class='css-1dbjc4n r-18u37iz r-1w6e6rj']/div/a")
        following=ss[0].get_attribute("title")
        followers=ss[1].get_attribute("title")
        img=self.driver.find_elements_by_xpath(".//img[@class='css-9pa8cd']")[1].get_attribute("src")
        dic={
            "name":name,
            "nb_tweets":nb_tweets,
            "user_description":UserDescription,
            "data":data,
            "following":following,
            "followers":followers,
            "image":img
            }
        self.user_info=dic
        return(dic)
    def get_publications(self,user_id,n,comments):
        """function that return data about the first n posts of a user"""
        self.driver.get("https://twitter.com/"+str(user_id))
        dic={}
        self.users_url=[]
        for i in range(n):
            #print("pub"+str(i+1))
            time.sleep(3)
            try:
                wait = WebDriverWait(driver, 10)
                wait.until(EC.element_to_be_clickable((By.XPATH, li[i])))
            except:
                pass
            try:
                li=self.driver.find_elements_by_xpath(".//div[@class='css-1dbjc4n r-18u37iz r-1wtj0ep r-156q2ks r-1mdbhws']")
                li[i].click()
            except:
                self.driver.find_elements_by_xpath(".//div[@class='css-1dbjc4n r-1awozwy r-18kxxzh r-zso239']")[i].click()
            self.driver.implicitly_wait(1)
            po=self.get_post(driver=self.driver)
            if comments == "F":
                dic["post"+str(i+1)]=po
            else:
                co=self.get_comments(driver=self.driver)
                dic["post"+str(i+1)]=po
                dic1={"comments":co}
                dic.update(dic1)
            self.driver.back()
            time.sleep(1)
        self.posts=dic
        return(dic)
    def get_post(self,driver):
        """function that takes the id of a twitter post and return data about that post"""
        time.sleep(1)
        try:
            contenu1=self.driver.find_element_by_xpath(".//div[contains(@class ,'css-901oao r-hkyrab r-1k78y06 r-1blvdjr r-16dba41')]").text
        except:
            contenu1=self.driver.find_element_by_xpath(".//div[contains(@class ,'css-901oao r-hkyrab r-1qd0xha r-1blvdjr r-16dba41')]").text
        try:
            image=self.driver.find_element_by_xpath(".//img[@alt='Image']").get_attribute("src")
            image=self.driver.find_element_by_xpath(".//div/img[@class='css-9pa8cd']").get_attribute("src")
        except:
            image=""
        date=self.driver.find_element_by_xpath(".//div[contains(@class ,'css-901oao r-1re7ezh r-1qd0xha')]/span").text
        try:
            nb1=self.driver.find_elements_by_xpath(".//div[contains(@class ,'css-1dbjc4n r-1gkumvb r-1efd50x')]/div")[0].text
        except:
            nb1=0
        try:
            nb2=self.driver.find_elements_by_xpath(".//div[contains(@class ,'css-1dbjc4n r-1gkumvb r-1efd50x')]/div")[1].text
        except:
            nb2=0
        i=0
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Show more replies')]"))).click()
        except:
            pass
        dic={
                "contenu":contenu1,
                "image":image,
                "date":date,
                "Retweets and comments":nb1,
                "likes":nb2,
            }
        return(dic)
    def get_comments(self,driver):
        li=[]
        users_url=[]
        for i in range(n):
            try:
                a=self.driver.find_elements_by_xpath(".//article[contains(@class ,'css-1dbjc4n r-1loqt21')]")
                user=a[i].find_element_by_xpath(".//a[contains(@class ,'css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21')]").text
                user_url=a[i].find_element_by_xpath(".//a[contains(@class ,'css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21')]").get_attribute("href")
                users_url.append(user_url)
                try:
                    comment=a[i].find_element_by_xpath(".//div[contains(@class ,'css-901oao r-hkyrab r-1k78y06 r-a023e6')]").text
                except:
                    comment=a[i].find_element_by_xpath(".//div[contains(@class ,'css-901oao r-hkyrab r-1qd0xha r-a023e6')]").text
                element=a[i].find_element_by_xpath(".//a[contains(@class ,'r-1re7ezh r-1loqt21 ')]")
                self.driver.execute_script("arguments[0].scrollIntoView();",element)
                date=a[i].find_element_by_xpath(".//a[contains(@class ,'r-1re7ezh r-1loqt21 ')]").get_attribute("title")
                li.append([user,comment,date])
                i=i+1
            except:
                break
        return(li)
    def get_comment_by_publication(self,publication_id):
        self.driver.get(str(publication_id))
        li=[]
        time.sleep(3)
        for i in range(100):
            try:
                a=self.driver.find_elements_by_xpath(".//article[contains(@class ,'css-1dbjc4n r-1loqt21')]")
                user=a[i].find_element_by_xpath(".//a[contains(@class ,'css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21')]").text
                try:
                    comment=a[i].find_element_by_xpath(".//div[contains(@class ,'css-901oao r-hkyrab r-1k78y06 r-a023e6')]").text
                except:
                    comment=a[i].find_element_by_xpath(".//div[contains(@class ,'css-901oao r-hkyrab r-1qd0xha r-a023e6')]").text
                element=a[i].find_element_by_xpath(".//a[contains(@class ,'r-1re7ezh r-1loqt21 ')]")
                self.driver.execute_script("arguments[0].scrollIntoView();",element)
                date=a[i].find_element_by_xpath(".//a[contains(@class ,'r-1re7ezh r-1loqt21 ')]").get_attribute("title")
                li.append([user,comment,date])
                i=i+1
            except:
                pass
        return(li)
        
            
       
