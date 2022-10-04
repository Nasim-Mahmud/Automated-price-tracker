import requests
import pprint
from bs4 import BeautifulSoup

pp = pprint.PrettyPrinter(width=41, compact=True)
amazon_headers = {
    "Accept": "text/plain",
    "Accept-Charset": "utf-8",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Accept-Language": "en-US"
}
response = requests.get(url="https://www.amazon.com/Passport-Portable-External-Drive-Black/dp/B07VTWX8MN/ref=sr_1_2?crid=36YNTNF7YQBBU&keywords=portable+hdd&qid=1664903210&qu=eyJxc2MiOiI1LjU4IiwicXNhIjoiNC45MiIsInFzcCI6IjQuNTUifQ%3D%3D&refinements=p_89%3AWestern+Digital%2Cp_n_feature_five_browse-bin%3A2419645011%2Cp_n_feature_keywords_five_browse-bin%3A7688215011%2Cp_n_feature_two_browse-bin%3A5446812011&rnid=562234011&s=pc&sprefix=portable+hd%2Caps%2C332&sr=1-2",
                        headers=amazon_headers)

data = response.text
soup = BeautifulSoup(data, "lxml")

price = soup.find(name="span", class_="a-offscreen").text.replace("$","")
print(price)