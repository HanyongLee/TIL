# https://finance.naver.com/sise/에 요청을 보내서, 응답을 받아온다.

import requests # 나 대신 요청해서 가져와서 리턴해줘
import bs4

url = "https://finance.naver.com/sise/"
response = requests.get(url)
# print(response.text) #200 무조건 좋은 것, 404, 500 등등..

html = bs4.BeautifulSoup(response.text, 'html.prarser')
# print(html)
#

kospi = html.select_one('#KOSPI_now')
print(kospi.text)
