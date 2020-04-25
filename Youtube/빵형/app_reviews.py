from selenium import webdriver
from bs4 import BeautifulSoup
import time, os
from datetime import datetime
import pandas as pd 

link =  'https://play.google.com/store/apps/details?id=com.miso&hl=ko&showAllReviews=true'

scroll_cnt = 10

driver = webdriver.Chrome('./chromedriver')
driver.get(link)

# 여기까지 OK 
os.makedirs('result',exist_ok=True)

for i in range(scroll_cnt):
  # scroll to bottom
  driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
  time.sleep(3)

  try:
        load_more = driver.find_element_by_xpath('//*[contains(@class,"U26fgb O0WRkf oG5Srb C0oVfc n9lfJ")]').click()
  except:
        print('Cannot find load more button...')

# get review containers
reviews = driver.find_elements_by_xpath('//*[@jsname="fk8dgd"]//div[@class="d15Mdf bAhLNe"]')

print("%d개가 현재 가용합니다.!" % len(reviews))
print('데이터 작성중...')
df = pd.DataFrame(columns=['user_name','rating','date_of_rg','likes','cmnt','dlp_cmnt'])

for review in reviews:
    soup = BeautifulSoup(review.get_attribute('innerHTML'),('html.parser'))

    user_name = soup.find(class_='X43Kjb').text

    rating = int(soup.find('div',role='img').get('aria-label').replace('rating 5개 만점에', '').replace('개를 받았습니다.', '').strip())

    date_of_rg = soup.find(class_='p2TkOb').text
    date_of_rg = datetime.strptime(date_of_rg, '%Y년 %m월 %d일')
    date_of_rg = date_of_rg.strftime('%Y-%m-%d')

    likes = soup.find(class_='jUL89d y92BAb').text
    if not likes:
        likes = 0
    
    cmnt = soup.find('span', jsname='fbQN7e').text
    if not cmnt:
        cmnt = soup.find('span', jsname='bN97Pc').text

    dlp_cmnt = None
    dc_div = soup.find('div',class_='LVQB0b')
    if dc_div:
        dlp_cmnt = dc_div.text.replace('/n', ' ')

    df = df.append({
    'user_name': user_name,
    'rating': rating,
    'date_of_rg': date_of_rg,
    'likes': likes,
    'cmnt': cmnt,
    'dlp_cmnt': dlp_cmnt
  }, ignore_index=True)

filename = datetime.now().strftime('result/%Y-%m-%d_%H-%M-%S.csv')
df.to_csv(filename, encoding='utf-8-sig', index=False)
driver.stop_client()
driver.close()

print('완료!')