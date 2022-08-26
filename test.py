import requests
from bs4 import BeautifulSoup

stock = "동구바이오제약"

for i in range(1,3): #1~5페이지까지
    url = f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={stock}&sort=1&photo=0&field=0&pd=0&ds=&de=&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:dd,p:all,a:all&start={i}"
    #print(url)

    response = requests.get(url)

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit") #결과는 리스트로나온다
    for link in links:
        title = link.text
        url = link.attrs['href']
        print(title)
        print(url)
        print('\n')
