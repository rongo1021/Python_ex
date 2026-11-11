import requests
from bs4 import BeautifulSoup
종목들 = ['KR7005930003', 'KR7066570003', 'KR7005380001', 'KR7035720002', 'KR7034220004', 'KR7003490000']
파일 = open('now.txt','w')

def 현재가(종목들):
    데이터 = requests.get(f'https://stock.mk.co.kr/price/home/{종목들}')
    soup = BeautifulSoup(데이터.content, 'html.parser')
    파일.write(soup.find_all('span', id="stock_price")[0].text + '\n')

for i in 종목들 :
    현재가(i)
파일.close()