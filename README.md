A crawler which extract data from a twitter Profile:
data extracted:

*profile description:
{-profile description
-image url
-name
...
}
*posts:
{
-date
-contenu
-comments
...
}

PS:to run this script go inside Crawler folder and then run this command : python __main__.py --url="A" --n=B --usr="C" --pwd="D"
where:
	A=url of the user
	B=number of posts to scrape
	C=twitter id
	D=twitter password

a folder "data" will be created and inside it you will find multiple folder named X(the name of the user) and inside each one you will
find images and json file contains data about the user X 