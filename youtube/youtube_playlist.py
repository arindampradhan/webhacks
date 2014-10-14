import requests
from bs4 import BeautifulSoup

url = raw_input("Enter the playlist url ->")
page = requests.get(url).text

soup = BeautifulSoup(page)
urls = soup.find_all('td',class_="pl-video-title")

links = []
for u in urls:
    links.append('https://www.youtube.com'+u.links['href'])

with open('youtube_playlist.txt','w') as f:
    for n in links:
        f.write(str(n))
        f.write('\n')
