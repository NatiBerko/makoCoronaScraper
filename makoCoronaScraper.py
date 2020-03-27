import requests
from requests_html import HTML

try:
    mako_response = requests.get("https://corona.mako.co.il/")
    mako_response.raise_for_status()
except requests.exceptions.HTTPError as err:
    raise SystemExit(err)

html_page = HTML(html=mako_response.text)

matches = html_page.find('div.stats-box')
parsed_dict = {}

for i in range(0, 3):
    x = matches[i].text.split('\n')
    parsed_dict[x[0]] = x[1]

for item in parsed_dict:
    print(item)
    print(parsed_dict[item])



