import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import pyautogui as pg

#record_audio.py에서 깐 것
import wave
from pyaudio import PyAudio, paComplete, paContinue, paInt16
from PIL import ImageGrab
import numpy as np
import cv2
from moviepy.editor import *
from moviepy.audio.fx import all
import pyaudio      

###########################
def collabo(user_id, user_pw, sub):

    #기초설정부분
    URL = 'https://kulms.korea.ac.kr/'
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path='/Hackerton/Hackerton_project/hyproject/hyapp/chromedriver', options=options)
    
    # <-여기 부분 컴퓨터랑 상관 없이 전체화면 되도록 수정해야함(수정완료)
    driver.get(url=URL)
    driver.maximize_window()
    driver.implicitly_wait(30) # <- time.sleep 굉장히 좋지않은 코드라서, 이거 적용안되는 문제 해결해서 수정해야함.

    #블랙보드에 들어가는 과정
    login_process1=driver.find_element_by_xpath('//*[@id="modalPush"]/div/div/div[1]/button/span[2]')
    login_process1.click()
    login_process2=driver.find_element_by_xpath('/html/body/div[2]/div/div/section/div/div/div/div[1]/div/div[2]/h3/strong/a')
    login_process2.click()
    login_id=driver.find_element_by_xpath('//*[@id="one_id"]')
    login_id.send_keys(user_id) #(여기 논의 필요) 사용자로부터 아이디를 입력받고, 데이터베이스에 저장해놨다가 그걸 가져와서 사용하는 방법
    login_password=driver.find_element_by_xpath('//*[@id="password"]')
    login_password.send_keys(user_pw)  #사용자로부터 비밀번호를 입력받고, 데이터베이스에 저장해놨다가 그걸 가져와서 쓰는 방법?
    login_password.send_keys(Keys.RETURN)
    time.sleep(10)
    click_course = driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[4]/div/li/a/ng-switch/div/span')
    click_course.click()
    time.sleep(10)

    #블랙보드<코스>항목을 클릭해 접속한 상태
    specific_subject = driver.find_element_by_partial_link_text(sub)
    #specific_subject=driver.find_element_by_xpath('//*[@id="course-link-_225509_1"]/h4')
    #specific_subject=driver.find_element_by_xpath(f"//*[text()={sub}]")#어떤 과목에 들어갈지는 역시 사용자로부터 입력받고 그것을 데이터베이스에서 가져와야함. (여기 조금 애매하다, 다른 함수로 분리해야하나?)
    #driver.findElement(By.xpath("//*[text()='"]"));
    specific_subject.click()
    time.sleep(10)

    #콜라보로 들어가는 부분
    button=pg.locateOnScreen("hyproject\hyapp\collabo.png")
    center=pg.center(button)
    pg.click(center)
    time.sleep(10)

    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="session-26a980f5466d4ea99a1a482c3cc00e58"]' ))).click()
    #find_collabo=driver.find_element_by_xpath('//*[@id="session-26a980f5466d4ea99a1a482c3cc00e58"]')
    #find_collabo.click()
    """
    button=driver.find_element_by_tag_name("button")
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(button).click(button).perform()
    """
    #html로 접근하는 것 일단 실패,그래도 다 책자모양 이미지 있으니까 그거 클릭해서 들어가게 해도 됨
    button=pg.locateOnScreen("hyproject\hyapp\\book.png")
    center=pg.center(button)
    pg.click(center)
    time.sleep(10)

    # join=driver.driver.find_element_by_xpath('//*[@id="integration-meeting-list"]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[4]/div/div/a').click()


    #여기도 일단 임시적으로 이미지로 접근하게 끔 만들어놓음(일단 되긴 됨)
    button=pg.locateOnScreen("hyproject\hyapp\gogo.png")
    center=pg.center(button)
    pg.click(center)
    time.sleep(20)

    #마이크 설정
    pg.press(['tab', 'tab', 'enter'])
    # button=pg.locateOnScreen("allow.png")
    # center=pg.center(button)
    # pg.click(center)
    time.sleep(5)

    #마이크 예 잘 작동함
    button=pg.locateOnScreen("hyproject\hyapp\yes.png")
    center=pg.center(button)
    pg.click(center)
    time.sleep(20)

    #카메라 설정
    pg.press(['tab', 'tab', 'enter'])
    # pg.press(['tab', 'tab', 'tab', 'enter'])
    time.sleep(10)
    button=pg.locateOnScreen("hyproject\hyapp\yes.png")
    center=pg.center(button)
    pg.click(center)
    time.sleep(10)
    #튜토리얼 창
    # pg.press(['tab','tab','tab', 'enter'])
    # time.sleep(5)
    # pg.press(['enter'])
    # time.sleep(5)
    button=pg.locateOnScreen("hyproject\hyapp\later.png")
    center=pg.center(button)
    pg.click(center)
    time.sleep(5)
    pg.press(['enter'])

    #####여기서부터 audio, 녹화하는 부분#####
    chunk=1024
    format= pyaudio.paInt16
    channels=2
    rate=44100

    # 이름은 과목 이름으로 (추후 변수로 저장)
    wave_output_filename="output.wav"
    p=pyaudio.PyAudio()
    wf=wave.open (wave_output_filename, "wb")
    wf.setnchannels (channels)
    wf.setsampwidth (p.get_sample_size(format))
    wf.setframerate (rate)
    audio_record_flag=True

    def callback (in_data, frame_count, time_info, status):
        wf.writeframes (in_data)
        if audio_record_flag:
            return (in_data, pyaudio.paContinue)
        else:
            return (in_data, pyaudio.paComplete)


    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), input=True, stream_callback=callback)

    # get the current screen
    image=ImageGrab.grab()
    width=image.size[0]
    height=image.size[1]
    print ("width:", width, "height:", height)
    print ("image mode:", image.mode)
    k=np.zeros ((width, height), np.uint8)
    fourcc= cv2.VideoWriter_fourcc(* "xvid") #encoding format
    video=cv2.VideoWriter("test.mp4", fourcc, 9.5, (width, height))
    #After actual testing,The maximum frame rate in a single thread is 10 frames/second, and it will change.

    #If the set frame rate is inconsistent with the actual frame rate,Will cause the video time to be inconsistent with the audio time
    print ("video recording !!!!!")
    stream.start_stream()
    print ("audio recording !!!!!")
    record_count=0

    while True:
        rgb=ImageGrab.grab()
        bgr=cv2.cvtColor(np.array(rgb), cv2.COLOR_RGB2BGR) #Convert to opencv's bgr format
        video.write(bgr)
        record_count +=1
        if (record_count>200):
            break
        print (record_count, time.time ())

    audio_record_flag=False
    while stream.is_active ():
        time.sleep (1)
        stream.stop_stream ()
        stream.close ()
        wf.close ()
        p.terminate ()
        print ("audio recording done !!!!!")
        video.release()
        cv2.destroyAllWindows()
        print ("video recording done !!!!!")
        print ("video audio merge !!!!!")
        audioclip= AudioFileClip("output.wav")
        videoclip= VideoFileClip("test.mp4")
        videoclip2= videoclip.set_audio (audioclip)
        video= CompositeVideoClip([videoclip2])
        video.write_videofile ("test2.mp4", codec="mpeg4")


def zoom(user_id, user_pw, sub):
    #기초설정부분
    URL = 'https://kulms.korea.ac.kr/'
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path='/Hackerton/Hackerton_project/hyproject/hyapp/chromedriver', options=options)
    driver.get(url=URL)
    driver.maximize_window()
    driver.implicitly_wait(20)

    #블랙보드에 들어가는 과정
    login_process1=driver.find_element_by_xpath('//*[@id="modalPush"]/div/div/div[1]/button/span[2]')
    login_process1.click()
    login_process2=driver.find_element_by_xpath('/html/body/div[2]/div/div/section/div/div/div/div[1]/div/div[2]/h3/strong/a')
    login_process2.click()
    login_id=driver.find_element_by_xpath('//*[@id="one_id"]')
    login_id.send_keys(user_id) #(여기 논의 필요) 사용자로부터 아이디를 입력받고, 데이터베이스에 저장해놨다가 그걸 가져와서 사용하는 방법
    login_password=driver.find_element_by_xpath('//*[@id="password"]')
    login_password.send_keys(user_pw)  #사용자로부터 비밀번호를 입력받고, 데이터베이스에 저장해놨다가 그걸 가져와서 쓰는 방법?
    login_password.send_keys(Keys.RETURN)
    time.sleep(10)
    click_course = driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[4]/div/li/a/ng-switch/div/span')
    click_course.click()
    time.sleep(10)

    #블랙보드<코스>항목을 클릭해 접속한 상태
    #specific_subject=driver.find_element_by_xpath('//*[@id="course-link-_223645_1"]/h4')#어떤 과목에 들어갈지는 역시 사용자로부터 입력받고 그것을 데이터베이스에서 가져와야함. (여기 조금 애매하다, 다른 함수로 분리해야하나?)
    specific_subject = driver.find_element_by_partial_link_text(sub)
    #specific_subject=driver.find_element_by_xpath(f"//*[text()={sub}]")#어떤 과목에 들어갈지는 역시 사용자로부터 입력받고 그것을 데이터베이스에서 가져와야함. (여기 조금 애매하다, 다른 함수로 분리해야하나?)
    specific_subject.click()
    time.sleep(8)
    button=pg.locateOnScreen("hyproject\hyapp\zoom.png")
    #button=pg.locateOnScreen("zoom.png")
    center=pg.center(button)
    pg.click(center)
    time.sleep(10)

    #xpath로 하는 방식이 안된다..왜지? -> 일단은 img 파일로 찾는걸로 !
    # zoom=driver.find_element_by_xpath('')
    # time.sleep(2)
    # zoom.click()

    button=pg.locateOnScreen("hyproject\hyapp\join.png") #임시로 join이미지로 접근하기로 했는데, 제일 상단 요소 찾아서 클릭해주기는 함. 하지만 실제 당일날 zoom화면이 어떻게 구성되는지 알아야함.
    center=pg.center(button)
    pg.click(center)
    time.sleep(10)
    #zoom화면에서 "zoom meetings 열기"  팝업창 버튼 클릭하는 과정(이후 줌 강의실로 들어가게 됨)
    button=pg.locateOnScreen("hyproject\hyapp\OpenZoom.png") 
    center=pg.center(button)
    print(center)
    pg.click(center) #여기까지 잘 됨
    ################################################################
    #여기부터 테스트 필요
    pg.press(['tab','tab','enter'])
    # zoom maximize
    w = pg.getWindowsWithTitle("Zoom 회의")[0]
    if w.isMaximized == False : 
        w.maximize()

    # default : 비디오 사용XS
    pg.press(['tab','tab','tab', 'tab', 'tab', 'enter'])

    # 수업주의사항 창이 뜰 경우 : 네

    # 오디오설정 클릭하기

    # 녹화 시작

    ######여기서부터 audio.py추가한부분 #####
    chunk=1024
    format= pyaudio.paInt16
    channels=2
    rate=44100

    # 이름은 과목 이름으로 (추후 변수로 저장)
    wave_output_filename="output.wav"
    p=pyaudio.PyAudio()
    wf=wave.open (wave_output_filename, "wb")
    wf.setnchannels (channels)
    wf.setsampwidth (p.get_sample_size(format))
    wf.setframerate (rate)
    audio_record_flag=True

    def callback (in_data, frame_count, time_info, status):
        wf.writeframes (in_data)
        if audio_record_flag:
            return (in_data, pyaudio.paContinue)
        else:
            return (in_data, pyaudio.paComplete)


    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), input=True, stream_callback=callback)

    # get the current screen
    image=ImageGrab.grab()
    width=image.size[0]
    height=image.size[1]
    print ("width:", width, "height:", height)
    print ("image mode:", image.mode)
    k=np.zeros ((width, height), np.uint8)
    fourcc= cv2.VideoWriter_fourcc(* "xvid") #encoding format
    video=cv2.VideoWriter("test.mp4", fourcc, 9.5, (width, height))
    #After actual testing,The maximum frame rate in a single thread is 10 frames/second, and it will change.

    #If the set frame rate is inconsistent with the actual frame rate,Will cause the video time to be inconsistent with the audio time
    print ("video recording !!!!!")
    stream.start_stream()
    print ("audio recording !!!!!")
    record_count=0

    while True:
        rgb=ImageGrab.grab()
        bgr=cv2.cvtColor(np.array(rgb), cv2.COLOR_RGB2BGR) #Convert to opencv's bgr format
        video.write(bgr)
        record_count +=1
        if (record_count>200):
            break
        print (record_count, time.time ())

    audio_record_flag=False
    while stream.is_active ():
        time.sleep (1)
        stream.stop_stream ()
        stream.close ()
        wf.close ()
        p.terminate ()
        print ("audio recording done !!!!!")
        video.release()
        cv2.destroyAllWindows()
        print ("video recording done !!!!!")
        print ("video audio merge !!!!!")
        audioclip= AudioFileClip("output.wav")
        videoclip= VideoFileClip("test.mp4")
        videoclip2= videoclip.set_audio (audioclip)
        video= CompositeVideoClip([videoclip2])
        video.write_videofile ("test2.mp4", codec="mpeg4")

collabo(sub)