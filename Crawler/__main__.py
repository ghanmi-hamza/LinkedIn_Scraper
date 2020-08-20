from myClass import *

@click.command()
@click.option('--url', default='', help='url of the user')
@click.option('--n', default=1, help='number of posts')
@click.option('--usr', default="", help="your Twitter login")
@click.option('--pwd', default="", help='password')

def main(url,n,usr,pwd):
    driver=get_browser(url,usr,pwd,chrome_path=chrome_path)
    p = Personne()
    p.user_data(driver,url)
    p.posts_details(url,driver,n)
    
    dic=p.user_info
    dic1={"posts":p.posts}
    dic.update(dic1)
    save_data(dic,dic["name"],r"C:\Users\Hamza\Desktop\Twitter_Crawler\Twitter_Crawler\data\.")
    li=list(set(p.users_url))
    print(li)
    for e in li:
        try:
            p1 = Personne()
            p1.user_data(driver,e)
            p1.posts_details(e,driver,n)
            dic=p1.user_info
            dic1={"posts":p1.posts}
            dic.update(dic1)
            save_data(dic,dic["name"],r"C:\Users\Hamza\Desktop\Twitter_Crawler\Twitter_Crawler\data\.")
            lj=list(set(p1.users_url))
            for m in lj:
                try:
                    p2 = Personne()
                    p2.user_data(driver,m)
                    p2.posts_details(m,driver,n)
                    dic=p2.user_info
                    dic1={"posts":p2.posts}
                    dic.update(dic1)
                    save_data(dic,dic["name"],r"C:\Users\Hamza\Desktop\Twitter_Crawler\Twitter_Crawler\data\.")
                except:
                    pass
                
        except:
            pass
        
if __name__=='__main__':
    main()
