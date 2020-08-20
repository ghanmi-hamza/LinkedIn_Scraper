from functions import *
class Personne():
    def __init__(self):
        """Constructeur de notre classe"""
        pass
        
    def user_data(self,driver,url):
        """function that takes the url of the user and return some info about it"""
        driver.get(url)
        time.sleep(3)
        c=driver.find_element_by_xpath(".//div[@class='css-1dbjc4n r-1habvwh']").text
        name=c.split("\n")[0]
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
        #return(dic)
    def posts_details(self,url,driver,n):
        """function that return data about the first n posts of a user"""
        driver.get(url)
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
            c=post_detail(driver=driver)
            dic["post"+str(i+1)]=c[0]
            self.users_url+=c[1]
            driver.back()
        self.posts=dic
        #return(dic)
        
       
