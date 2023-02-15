from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from translators import translate_text
from bs4 import BeautifulSoup

br = webdriver.Firefox()
br.get('http://www.classcentral.com/')
time.sleep(10)
html = br.page_source
html = html.replace('"/','"https://www.classcentral.com/')
soup = BeautifulSoup(html, 'lxml')
urls = []
for link in soup.find_all('a'):
    urls.append(link.get('href'))
with open("all_links.txt", 'w') as f:
    f.write("\n".join(urls))
tags = ['p','button','a','span','h2','h3','h5','time','i','div','strong']
for tag in tags:
    objects = soup.findAll(tag)
    for el in objects:
        if el.string!=None: 
            try: el.string.replace_with(translate_text(el.text,'google','en-US','hi'))
            except: continue

with open('main_new2.html','w', encoding='utf-8') as f:
    f.write(str(soup))

save_me = ActionChains(br).key_down(Keys.CONTROL)\
         .key_down('s').key_up(Keys.CONTROL).key_up('s')
save_me.perform()
br.close()