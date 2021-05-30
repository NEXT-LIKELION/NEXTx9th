from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def crawling(bbid, bbpassword):
    option = Options()

    option.add_argument("--headless")
    option.add_argument("start-maximised")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--window-size=1920x1080")

    prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
    option.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=option)

    WebDriverWait(driver, 5)

    driver.implicitly_wait(3)
    driver.get('https://kulms.korea.ac.kr/ultra/course')

    a= driver.find_element_by_xpath('//*[@id="modalPush"]/div/div/div[1]/button')
    driver.execute_script("arguments[0].click();", a)
    b= driver.find_element_by_xpath('/html/body/div[2]/div/div/section/div/div/div/div[1]/div/div[2]/h3/strong/a')
    driver.execute_script("arguments[0].click();", b)


    driver.find_element_by_name('one_id').send_keys(bbid)
    driver.find_element_by_name('user_password').send_keys(bbpassword+'\n')

    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to_alert
        return False
    except:
        print("성공")
        
    # element = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.XPATH,"//*[@id='base_tools']/bb-base-navigation-button[4]/div/li/a"))
    #     )

    # ####################################################################

    # driver.get('https://kulms.korea.ac.kr/ultra/course')

    driver.implicitly_wait(60)

    driver.execute_script("window.scrollTo(0, 900);")

    driver.implicitly_wait(60)

    lec_list = driver.find_elements_by_class_name("course-id")

    def data(lec_list):
        final_result = []
        for lec in lec_list:
            course_id = lec.text
            subnum = course_id[10:-2]+"-"+course_id[-2:]
            semester = course_id[0:6]

            if(semester == "20211R"):
                final_result.append(subnum)

        return final_result

    final_result = data(lec_list)

    return final_result

