from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from translators import translate_text
from bs4 import BeautifulSoup
import os

br = webdriver.Firefox()
#br.get('http://www.classcentral.com/')
#time.sleep(10)
#html = br.page_source
#homepage = html.replace('"/','"https://www.classcentral.com/')
homepage = open("main.html","r",encoding='utf-8').read()
soup = BeautifulSoup(homepage, 'lxml')
"""
tags = ['p','button','a','span','h2','h3','h5','time','i','div','strong']
for tag in tags:
    objects = soup.findAll(tag)
    for el in objects:
        if el.string!=None: 
            try: el.string.replace_with(translate_text(el.text,'google','en-US','hi'))
            except: continue

with open('main_new2.html','w', encoding='utf-8') as f:
    f.write(str(soup))
"""
soup_home = soup
urls = ["https://www.classcentral.com/"]
i = 0
translations = {}
pages = soup_home.find_all('a')
for link in pages:
    if link.get('href').startswith("https://www.classcentral.com/") and i not in (271,351):
        if link.get('href') == "https://www.classcentral.com/":
            link['href'] = link['href'].replace(link.get('href'),"main.html")
        
        else:
            to_save = link.get('href').replace("https://www.classcentral.com/","").replace("/","-")
            new_link = f'pages/{to_save}.html'
            if to_save+".html" in os.listdir("./pages") or link.get('href') in urls:
                link['href'] = link['href'].replace(link.get('href'),new_link)
            else:
                
                br.get(link.get('href'))
                time.sleep(5)
                html = br.page_source
                html = html.replace('"/','"https://www.classcentral.com/')
                
                soup = BeautifulSoup(html, 'lxml')
                """

                tags = ['p','button','a','span','h2','h3','h5','time','i','div','strong']
                for tag in tags:
                    objects = soup.findAll(tag)
                    for el in objects:
                        if el.string!=None: 
                            if el.text in translations.keys():
                                el.string.replace_with(translations[el.text])
                            else:
                                try:
                                    translation = translate_text(el.text,'google','en-US','hi') 
                                    el.string.replace_with(translation)
                                    translations[el.text] = translation
                                except: continue
                """
                with open(new_link,'w', encoding='utf-8') as f:
                    f.write(str(soup))
                link['href'] = link['href'].replace(link.get('href'),new_link)
                urls.append(link.get('href'))
        print(link.get('href'))
        print(f"Completed {i}/{len(pages)}")
    i+=1

with open("all_links.txt", 'w') as f:
    f.write("\n".join(urls))

with open('main2.html','w', encoding='utf-8') as f:
    f.write(str(soup_home))

save_me = ActionChains(br).key_down(Keys.CONTROL)\
         .key_down('s').key_up(Keys.CONTROL).key_up('s')
save_me.perform()
br.close()