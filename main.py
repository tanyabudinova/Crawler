import requests
from bs4 import BeautifulSoup
import re

start = "https://register.start.bg/"
r = requests.get(start)

soup = BeautifulSoup(r.text, 'html.parser')

pattern_js = re.compile(r"^javascript:.*")
pattern_hash = re.compile(r"^#.*")
pattern_http = re.compile(r"^https?://.*")
links = []
for link in soup.find_all('a'):
    link = link.get('href')
    if link is None:
        continue
    if link in links:
        continue
    if pattern_js.match(link):
        continue
    if pattern_hash.match(link):
        continue
    if not pattern_http.match(link):
        link = start + link
    links.append(link)
    print(link)
