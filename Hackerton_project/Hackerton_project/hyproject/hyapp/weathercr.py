import requests
from bs4 import BeautifulSoup as bs

"""해커톤 때 
1.'당일'요일만 받아와서 마저 처리
3. 정보 넘겨주는 것 받는 사람이랑 이야기
"""
URL="https://weather.com/ko-KR/weather/tenday/l/d034b23583dc5e5d518c597ff34a5e19aa21c3fc3012660882f72bd3c8014ff2"

def weathercrcr():
 weather_html=requests.get(URL)
 weather_soup=bs(weather_html.text, "html.parser")
 best_weather=[]
 result = []
 #오늘 날씨의 데이터 받아오기
 today_soup=weather_soup.find('div', {'data-testid':'DailyContent'})
 today_a=today_soup.find('span',{'class':'DailyContent--daypartDate--3MM0J'}).text #오늘 날짜
 today_b=today_soup.find('span',{'data-testid':'TemperatureValue'}).text #오늘 기온
 today_c=today_soup.find('span', {'data-testid':'PercentageValue'}).text #오늘 강수확률
 if (int(today_b.replace("°","")) <30) and (int(today_c.replace("%","")) <30 ):
    best_weather += [[today_a] + [today_b] + [today_c]]


 #향후 6일간의 날짜 데이터 받아오기(string으로 받아오면 bs4객체고, text로 받아오면 str객체)
 for i in range(1,7):
     id_name=f'detailIndex{i}'
     a=weather_soup.find('div', {'id':id_name}) 
     b=str(a.find('h2',{'class':'DetailsSummary--daypartName--1Mebr'}).string) 
     c=a.find('span', {'class':'DetailsSummary--highTempValue--3x6cL'}).text 
     d=a.find('span', {'data-testid':'PercentageValue'}).text 
     if (int(c.replace("°","")) <30) and (int(d.replace("%","")) <30 ):
         result += [[b] + [c] + [d]] 
 result += best_weather
         
 return result


#
#beat_weather 변수 안에 걸러진 요일, 기온, 강수확률 정보 다 담겨있음!