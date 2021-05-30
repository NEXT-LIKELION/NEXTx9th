import time
import django
django.setup()

from .models import Subject

# selenium 가져오기
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup

# 최초 사이트로 접속


def crawling(User, User_Id, User_Password):
 URL = 'https://kulms.korea.ac.kr/'

 options = webdriver.ChromeOptions()
 options.add_argument("--window-size=1920,1080")
 options.add_argument("--disable-extensions")
 options.add_argument("--proxy-server='direct://'")
 options.add_argument("--proxy-bypass-list=*")
 options.add_argument("--start-maximized")
 options.add_argument('--headless')
 options.add_argument('--disable-gpu')
 options.add_argument('--disable-dev-shm-usage')
 options.add_argument('--no-sandbox')
 options.add_argument('--ignore-certificate-errors')
 driver = webdriver.Chrome(executable_path='/Users/배윤주/Desktop/LIKE_LION/Hackerton/chromedriver', options=options)
#  , chrome_options=options
 driver.get(url=URL)
 time.sleep(2)

 # 첫 창 닫기
 logi_link = driver.find_element_by_xpath(
    '//*[@id="modalPush"]/div/div/div[1]/button/span[2]')
 driver.execute_script("arguments[0].click();", logi_link)
 time.sleep(4)
 
 # 블랙보드 로그인 창 이동
 driver.get_screenshot_as_file("screenshot1.png")
 login_link = driver.find_element_by_partial_link_text('블랙보드 로그인')
 driver.execute_script("arguments[0].click();", login_link)
 time.sleep(4)

 # 로그인 정보 입력 및 로그인 엔터
 input_id = driver.find_element_by_xpath('//*[@id="one_id"]')
 input_id.send_keys(User_Id)
 input_password = driver.find_element_by_xpath('//*[@id="password"]')
 input_password.send_keys(User_Password)
 driver.get_screenshot_as_file("screenshot1.png")
 input_password.send_keys(Keys.RETURN)
 time.sleep(8)

 # 코스 클릭
 click_course = driver.find_element_by_xpath(
     '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[4]/div/li/a/ng-switch/div/span')
 click_course.click()
 time.sleep(3)

 # 크롤링을 위한 준비

 # 이번 학기 과목이 담긴 div들

# 가장 아래로 스크롤 다운
#  driver.maximize_window();
 time.sleep(2)
#  driver.execute_script('window.scrollTo(0, 1080)')
#  driver.execute_script("arguments[0].scrollIntoView(true);", next_page_click_element)
 # 모든 과목이름을 로드하기 위해 스크롤 다운 (모든 아이디에 맞게 수정필요!!!!!)
 some_tag =  driver.find_element_by_xpath('//*[@id="course-card-term-name-_64_1"]/h3')
#  last_height = driver.execute_script("return document.body.scrollHeight")
#  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 action = ActionChains(driver)
 action.move_to_element(some_tag).perform()
 time.sleep(13)
 # 과목명 및 교수명 취합
 html = driver.page_source
 soup = BeautifulSoup(html, 'html.parser')
 course_div_list = soup.find_all("div", {"class": "default-group term-_70_1"})
#  result_subject = {}
 for course in course_div_list:
     title = course.find("a").find("h4").text.split(']')[1].split('(')[0]
     professor = course.find("div", {"class": "ellipsis"}).find("span")["aria-label-if-no-accommodation"].replace('.', '')
     find_subject = Subject.objects.filter(subject=title).filter(user=User)
     if find_subject.count() > 0:
         pass
     else:   
         Subject.objects.create(subject=title, professor=professor, user=User)
#      course_info = {
#          title,
#          professor,
#      }

#  for t, p in result_subject.items():
#      Subject(title=t, professor=p).save()





# 매 10초 마다 job함수 실행 schedule.every(10).seconds.do(job)

# while True:
#   schedule.run_pending()
