from bs4 import BeautifulSoup
import requests
response = requests.get(url="https://news.ycombinator.com/news")
response_text = response.text

soup = BeautifulSoup(response_text,'html.parser')
yc_links = soup.find_all(class_="storylink")
scores = soup.find_all(name='span',class_='score')
pscr = [ int(scr.text.split()[0]) for scr in soup.find_all(name='span',class_='score')]
print(pscr)
title=[]
links = []
for text in yc_links:
    title.append(text.getText())
for text in yc_links:
    links.append(text.get("href"))

maxind = pscr.index(max(pscr))
hig= max(pscr)
print(hig)
print(title[maxind])
print(links[maxind])
# with open('cv.html') as webfile:
#     webdata = webfile.read()
#
# soup = BeautifulSoup(webdata,"html.parser")
# # all_anchor_tags = soup.find_all(name='a')
# # print(all_anchor_tags)
# # for tag in all_anchor_tags:
# #     print(tag.get("href"))
# work = soup.find(class_="work-work",name="h3")
# print(work)