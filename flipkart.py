from urllib import request
from bs4 import BeautifulSoup
from urllib.request import Request

url = "https://www.amazon.in/s?k=iphone+14+pro&crid=1895G6V2AVMUW&sprefix=iph%2Caps%2C296&ref=nb_sb_ss_ts-doa-p_2_3"


request_site=Request(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})
html = request.urlopen(request_site).read()
soup = BeautifulSoup(html,"html.parser")
# print(soup)

def iphoneInfo():
    name=soup.find("span",{"class":"a-size-medium a-color-base a-text-normal"}).text
    price = soup.find("span", {"class": "a-offscreen"}).text
    rating = soup.find("span",{"class":"a-icon-alt"}).text
    return name,price,rating
name,price,rating=iphoneInfo()
print("Name : ",name)
print("Price : ",price)
print("Rating : ",rating)

urla = "https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX2F5QT/ref=sr_1_1_sspa?crid=1895G6V2AVMUW&keywords=iphone%2B14%2Bpro&qid=1700540983&sprefix=iph%2Caps%2C296&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

request_site=Request(urla,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})
html = request.urlopen(request_site).read()
soup = BeautifulSoup(html,"html.parser")

def memory():
    memories=soup.find("span",{"class":"a-size-base swatch-title-text-display swatch-title-text"}).text
    return memorie
memories=memory()
print("Memory : ",memories)
