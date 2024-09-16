#non-related: u can make .env file. put environment variables there like SOMETHING= "something"
#then import os
#from dotenv import load_dotenv
#load_dotenv()
#then just behave like os.environ["SOMETHING"]


from bs4 import BeautifulSoup
import requests

res=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/") #can have headers arg
web=res.text
soup=BeautifulSoup(web,"html.parser")
fobjs=soup.find_all('h3',class_='title')
films=[x.getText() for x in fobjs]
films=reversed(films)

with open("films.txt","w",encoding='utf-8') as f:
    for _ in films:
        f.write(f"{_}\n")
















#range(99,0,-1) # 0 becomes 1 #if it were -1, itd be 0
#list[::-1] #reversing

'''
res=requests.get("https://news.ycombinator.com/news")
web=res.text
soup=BeautifulSoup(web,"html.parser")

pelements=soup.find_all(class_='subtext')

points=[int(x.span.span.getText().split()[0]) if x.span.span else 0 for x in pelements] #.strip(' points')

highest=max(points)

index=points.index(highest)

telements=soup.find_all("span",class_="titleline")

titles=[x.getText() for x in telements]

print(titles[index])

links=[x.a.get("href") for x in telements]

print(links[index])
'''

'''
with open("website.html",encoding='utf8') as f:
    content=f.read()

soup=BeautifulSoup(content,"html.parser") #or "lxml"

print(content)
print("----------------")
print(soup)
print("----------------")
print(soup.prettify())
print(soup.h1)
print(soup.h1.name)
print(soup.h1.getText())
print(soup.h1.get("id"))
print(soup.find('p'))
print(soup.find('a',href="https://angelabauer.github.io/cv/hobbies.html"))
print(soup.find_all('a'))
print(soup.find_all('h3',class_='heading'))
print(soup.select_one('p a'))
print(soup.select('.heading'))

'''

#all_link_elements = soup.select(".StyledPropertyCardDataWrapper a") 
#all_links = [link["href"] for link in all_link_elements]
