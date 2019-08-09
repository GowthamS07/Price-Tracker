import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
url = "https://www.amazon.in/United-Colors-Benetton-Mens-Sneakers/dp/B0792DDS9C/ref=pd_sbs_309_41?_encoding=UTF8&pd_rd_i=B0792DDS9C&pd_rd_r=37f5a38e-7aec-4629-a13c-e0275af08fe8&pd_rd_w=UmPpQ&pd_rd_wg=TNla8&pf_rd_p=5c023088-3bf1-437a-ba7d-b879da18a58e&pf_rd_r=0HT9K76XMP84AZY2A5Y7&refRID=0HT9K76XMP84AZY2A5Y7"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}

def check_price(url, headers):
    page = requests.get(url , headers= headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    print(title.strip())
    
    try:
        price = soup.find(id="priceblock_ourprice").get_text()
        print(price.strip())
    except AttributeError:
        print("price = _")

    try:
        price = soup.find(id="priceblock_dealprice").get_text()
        print(price.strip())
    except AttributeError:
        print("price = _")

    price = list(price)
    price[3] = '.'

    conv_price = float("".join(price[2:7]))
    print(conv_price)

    if(conv_price < 1.899):
        sendsms()

def sendsms():
    client = Client('AXXXXXXXXXXXXXXXXXXXXXXXX', '1XXXXXXXXXXXXXXXXXXXXXXX')
    client.messages.create(to = '+91XXXXXXXXXX', from_ = '+1XXXXXXXXXX', body = 'Price reduced: https://www.amazon.in/United-Colors-Benetton-Mens-Sneakers/dp/B0792DDS9C/ref=pd_sbs_309_41?_encoding=UTF8&pd_rd_i=B0792DDS9C&pd_rd_r=37f5a38e-7aec-4629-a13c-e0275af08fe8&pd_rd_w=UmPpQ&pd_rd_wg=TNla8&pf_rd_p=5c023088-3bf1-437a-ba7d-b879da18a58e&pf_rd_r=0HT9K76XMP84AZY2A5Y7&refRID=0HT9K76XMP84AZY2A5Y7')

check_price(url, headers)
