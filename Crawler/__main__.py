from myClass import *

@click.command()
@click.option('--url', default='', help='url of the user')
@click.option('--n', default=1, help='number of posts')
@click.option('--s', default=False, help='Download data')
@click.option('--usr', default="", help="your Twitter login")
@click.option('--pwd', default="", help='password')

def main(url,n,s,usr,pwd):
    
    driver=get_browser(url,usr,pwd)
    p = TwitterDriver()
    p.get_user_info(driver,url)
    p.get_publications(url,driver,n)
    
    dic=p.user_info
    dic1={"posts":p.posts}
    dic.update(dic1)
    if s=="True":
        save_data(dic,dic["name"],r"C:\Users\Hamza\Desktop\Twitter_Crawler\Twitter_Crawler\data\.")
    else:
        pass
    li=list(set(p.users_url))
    print(li)
    for e in li:
        try:
            p1 = TwitterDriver()
            p1.get_user_info(driver,e)
            p1.get_publications(e,driver,n)
            dic=p1.user_info
            dic1={"posts":p1.posts}
            dic.update(dic1)
            if s=="True":
                save_data(dic,dic["name"],r"C:\Users\Hamza\Desktop\Twitter_Crawler\Twitter_Crawler\data\.")
            else:
                pass
            lj=list(set(p1.users_url))
            for m in lj:
                try:
                    p2 = TwitterDriver()
                    p2.get_user_info(driver,m)
                    p2.get_publications(m,driver,n)
                    dic=p2.user_info
                    dic1={"posts":p2.posts}
                    dic.update(dic1)
                    if s=="True":
                        save_data(dic,dic["name"],r"C:\Users\Hamza\Desktop\Twitter_Crawler\Twitter_Crawler\data\.")
                    else:
                        pass
                except:
                    pass
                
        except:
            pass
        
if __name__=='__main__':
    main()
