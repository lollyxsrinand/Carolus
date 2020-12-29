import requests
from bs4 import BeautifulSoup
import re
search = input("Search:")
count = 1
results = 8 # valid options 10, 20, 30, 40, 50, and 100
page = requests.get(f"https://www.google.com/search?q={search}&num={results}")
soup = BeautifulSoup(page.content, "html.parser")
links = soup.findAll("a")
for link in links :
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
        print (count)
        print (link.get('href').split("?q=")[1].split("&sa=U")[0])
        count += 1
