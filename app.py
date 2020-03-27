import requests
from bs4 import beautifulsoup as bs4
import urllib

query = input("type your querry")
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"

# Desktop User Agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

headers = {"user-agent": MOBILE_USER_AGENT}
resp = requests.get(URL, headers=headers)

if resp.status_code == 200:
    soup = bs(resp.content, "html.parser")

results = []
for g in soup.find_all('div', class_='r'):
    anchors = g.find_all('a')
    if anchors:
        link = anchors[0]['href']
        title = g.find('h3').try:
            item = {
                "title": title,
                "link": link
            }
            results.append(item)

print(results)
