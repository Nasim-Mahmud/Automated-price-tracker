import os
from smtplib import *
import requests
from bs4 import BeautifulSoup

EXPECTED_PRICE = 60

amazon_headers = {
    "Accept": "text/plain",
    "Accept-Charset": "utf-8",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Accept-Language": "en-US"
}
response = requests.get(
    url="https://www.amazon.com/Passport-Portable-External-Drive-Black/dp/B07VTWX8MN/ref=sr_1_2?crid=36YNTNF7YQBBU&keywords=portable+hdd&qid=1664903210&qu=eyJxc2MiOiI1LjU4IiwicXNhIjoiNC45MiIsInFzcCI6IjQuNTUifQ%3D%3D&refinements=p_89%3AWestern+Digital%2Cp_n_feature_five_browse-bin%3A2419645011%2Cp_n_feature_keywords_five_browse-bin%3A7688215011%2Cp_n_feature_two_browse-bin%3A5446812011&rnid=562234011&s=pc&sprefix=portable+hd%2Caps%2C332&sr=1-2",
    headers=amazon_headers)

data = response.text
soup = BeautifulSoup(data, "lxml")

product_name = soup.find(name="span", id="productTitle").text.strip()
# print(product_name)
price = float(soup.find(name="span", class_="a-offscreen").text.replace("$", ""))
# print(price)
price_symbol = soup.find(name="span", class_="a-price-symbol").text
# print(price_symbol)

my_email = os.environ["myEmail"]
my_pass = os.environ["myPass"]
test_email = os.environ["testEmail"]
if price <= EXPECTED_PRICE:
    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs=test_email,
                            msg="Subject: Lowest Price alert!\n\n"
                                f"Hey Buddy,\n"
                                f"The price of {product_name} is down to {price_symbol}{price}!\n"
                                f"It's the perfect time to buy it."
                            )
