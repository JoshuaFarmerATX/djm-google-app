import requests, webbrowser
from bs4 import BeautifulSoup as bs
from pprint import pprint
import csv

def export_dict_list_to_csv(data, filename):
    with open(filename, 'w+', newline='') as f:
        # Assuming that all dictionaries in the list have the same keys.
        # headers = sorted([k for k, v in data[0].items()])
        headers = (['Search', 'Title', 'Link', 'Description'])
        csv_data = [headers]

        for d in data:
            csv_data.append([d[h] for h in headers])

        writer = csv.writer(f)
        writer.writerows(csv_data)

query = input("type search criteria: ")
query = query.replace(" ", "+")

URL = f'https://google.com/search?q={query}'
headers = {
  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0"
}
response = requests.get(URL, headers=headers)
soup = bs(response.text, "html.parser")
# print(soup)

# for item in soup.find_all(class_='g'):
#     pprint(item.text)
search_dict = []
for items in soup.find_all(class_='g'):
  for item in items(class_="LC20lb DKV0Md"):
    link_title = item.text
  for item in items(class_="st"):
    link_desc = item.text
  for item in items(class_='iUh30 bc tjvcx'):
    link_href = item.text.split(" ", 1)[0]
  search_dict.append({
    'Search': query.replace("+", " "),
    'Title': link_title,
    'Description': link_desc,
    'Link': link_href
  })

  export_dict_list_to_csv(search_dict, 'search.csv') 