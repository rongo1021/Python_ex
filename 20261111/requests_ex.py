import requests
import urllib.request
from bs4 import BeautifulSoup

데이터 = requests.get('https://stock.mk.co.kr/price/home/KR7005930003')
soup = BeautifulSoup(데이터.content, 'html.parser')
print(soup.find_all('span', id="stock_price")[0].text)

urllib.request.urlretrieve('https://stock.mk.co.kr/uploads/20261111/1794363343_bb739984c5a99cf6f297.pdf', 'ex_0001.pdf')