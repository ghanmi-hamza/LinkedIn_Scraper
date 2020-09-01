from functions import *
from abc import ABC
class Driver(ABC):

    def get_user_info(self,driver,url):
        pass
    
    def get_publications(self,url,driver,n):
        pass
    
    def get_post(self,driver):
        pass

    def get_comments(self,driver):
        pass
class TwitterDriver(Driver):
    def __init__(self):
        """Constructeur de notre classe"""
        pass
        
    def get_user_info(self,driver,url):
        """function that takes the url of the user and return some info about it"""
        driver.get(url)
        time.sleep(3)
        c=driver.find_element_by_xpath(".//div[@class='css-1dbjc4n r-1habvwh']").text
        name=c.split("\n")[0]
        print(name)
        nb_tweets=c.split("\n")[1]
        tagName=driver.find_element_by_xpath(".//div[@class='css-1dbjc4n r-18u37iz r-1wbh5a2']").text
        UserDescription=driver.find_element_by_xpath(".//div[@data-testid='UserDescription']").text
        data=driver.find_element_by_xpath(".//div[@data-testid='UserProfileHeader_Items']").text
        ss=driver.find_elements_by_xpath(".//div[@class='css-1dbjc4n r-18u37iz r-1w6e6rj']/div/a")
        following=ss[0].get_attribute("title")
        followers=ss[1].get_attribute("title")
        img=driver.find_elements_by_xpath(".//img[@class='css-9pa8cd']")[1].get_attribute("src")
        dic={
            "name":name,
            "tag_name":tagName,
            "nb_tweets":nb_tweets,
            "user_description":UserDescription,
            "data":data,
            "following":following,
            "followers":followers,
            "image":img
            }
        self.user_info=dic
    def get_publications(self,url,driver,n):
        """function that return data about the first n posts of a user"""
        
        dic={}
        self.users_url=[]
        for i in range(n):
            print("-------------------------------------")
            time.sleep(2)
            try:
                wait = WebDriverWait(driver, 10)
                wait.until(EC.element_to_be_clickable((By.XPATH, li[i])))
            except:
                pass
            try:
                li=driver.find_elements_by_xpath(".//div[@class='css-1dbjc4n r-18u37iz r-1wtj0ep r-156q2ks r-1mdbhws']")
                li[i].click()
            except:
                driver.find_elements_by_xpath(".//div[@class='css-1dbjc4n r-1awozwy r-18kxxzh r-zso239']")[i].click()
            driver.implicitly_wait(1)
            c=self.get_post(driver=driver)
            print(c)
            dic["post"+str(i+1)]=c[0]
            self.users_url+=c[1]
            driver.back()
            time.sleep(1)
        self.posts=dic
    def get_post(self,driver):
        """function that takes the id of a twitter post and return data about that post"""
        time.sleep(1)
        try:
            contenu1=driver.find_element_by_xpath(".//div[contains(@class ,'css-901oao r-hkyrab r-1k78y06 r-1blvdjr r-16dba41')]").text
        except:
            contenu1=driver.find_element_by_xpath(".//div[contains(@class ,'css-901oao r-hkyrab r-1qd0xha r-1blvdjr r-16dba41')]").text
        try:
            image=driver.find_element_by_xpath(".//img[@alt='Image']").get_attribute("src")
            image=driver.find_element_by_xpath(".//div/img[@class='css-9pa8cd']").get_attribute("src")
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
        li=self.get_comments(driver=driver)
        dic={
                "contenu":contenu1,
                "image":image,
                "date":date,
                "Retweets and comments":nb1,
                "likes":nb2,
                "comments":li[0]
            }
        return(dic,li[1])
    def get_comments(self,driver):
        li=[]
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
        return(li,users_url)
        
            
       
