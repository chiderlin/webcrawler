from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
driver=webdriver.Chrome()
driver.get("https://www.ettoday.net/?from=rf")
for i in range(0,2):
    html=driver.page_source
    sp=BeautifulSoup(html,"html.parser")
    sp1=sp.find("div","block block_1 infinite_scroll")
    sp2=sp1.find_all("a")
    for i in range(2,len(sp2)):
        print(sp2[i].text)
        print(sp2[i].get("href"))
        time.sleep(0.8)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(10)
driver.quit()