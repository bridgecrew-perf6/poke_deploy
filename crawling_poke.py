import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
import shutil

ChromeDriver = "C:\python\chromedriver.exe"
url = 'https://www.pokemonkorea.co.kr/pokedex#pokedex_154'
driver = webdriver.Chrome(executable_path=ChromeDriver)
driver.get("https://www.pokemonkorea.co.kr/pokedex")

# 스크롤코드
time.sleep(0.5)  # Allow 2 seconds for the web page to open
scroll_pause_time = 0.5 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
last_height = driver.execute_script("return document.body.scrollHeight")   # get the screen height of the web
while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
    time.sleep(scroll_pause_time)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break
    last_height = new_height
print("루프끝")

# 크롤링 코드
soup = BeautifulSoup(driver.page_source,"html.parser")
lists = soup.find_all('li',class_='col-lg-2 col-6')

for i in lists:
    img_url = i.find('img').get('src')
    img_url = requests.get(img_url, stream=True)
    name = i.find('h3').text
    add_name = i.find('h3').nextSibling.nextSibling.text
    name = name.replace('타입:널', '실버디')
    add_name = add_name.replace('/','_')
    add_name = add_name.replace('타입:노말','')
    if add_name != '':
        filename = f"{name}({add_name})"
    else:
        filename = name
    print(filename)
    with open(f"./image/{filename}.png",'wb') as f:
        shutil.copyfileobj(img_url.raw, f)

