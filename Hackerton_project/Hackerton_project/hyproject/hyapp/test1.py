from datetime import datetime
import time



while True:
    time.sleep(2)
    print("주송준트롤")
    print(datetime.now())
    if ((datetime.now().hour == 8) and (datetime.now().minute == 20)):
        print("if문실행됨")
        break
    print("안녕하세요")
