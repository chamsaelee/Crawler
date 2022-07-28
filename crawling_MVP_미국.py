import selenium
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import time, requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys
import urllib.request

keywords_prod = [
    "Abbott FreeStyle Libre", "Dexcom G6", "Dexcom G7", "Medtronic Guardian",
    "Apple Glucose", "Apple Blood sugar", "Samsung Glucose", "Samsung Blood sugar"
    "Cnoga Medical Hybrid Glucometer", "Integrity GlucoTrack",
    "Mediwise Glucowise", "Nemaura Sugarbeat", 
    "Quantum Operation Inc Glucose", "Quantum Operation Inc Blood sugar",
    "Dongwoon Anatech D-salife", "Alertgy ANICGM",
    "Igluco Tech Glucose", "Igluco Tech Blood sugar",
    "Afon Technology Glucose", "Afon Technology Blood sugar",
    "Opuz Glucose", "Opuz Blood sugar",
    "RSP Systems Glucose", "RSP Systems Blood sugar",
    "c8 medisensors Optical Glucose Monitor",
    "Gluco vista Glucose", "Gluco vista Blood sugar",
    "Fitbit Glucose", "Fitbit Blood sugar",
    "Rockley Glucose", "Rockley Blood sugar",
    "gramin Glucose", "gramin Blood sugar"
]

keywords_tech = [
    "Continuous glucose meter", "Continuous glucose monitoring",
    "Photoacoustic Glucose" , "Photoacoustic Blood sugar",
    "Optoacoustic Glucose", "Optoacoustic Blood sugar",
    "CGMS", "CGM",
    "Noninvasive Glucose", "Noninvasive Blood sugar",
    "Non-invasive Glucose", "Non-invasive Blood sugar",
    "Non invasive Glucose", "Non invasive Blood sugar",
    "Smartwatch Glucose", "Smartwatch Blood sugar",
    "Wearable Glucose", "Wearable Blood sugar"
]

keywords_policy = [
    "Diabetes Medical insurance", "Diabetes Health insurance", "Diabetes Health care",
    "FDA Diabetes", "FDA Glucose", "FDA Blood sugar", "FDA CGM", "FDA Glucose meter", "FDA Glucose monitoring",
    "Clinical study CGM", "Clinical study Glucose meter", "Clinical study Clucose monitoring",
    "Clinical trial CGM", "Clinical trial Glucose meter", "Clinical trial Glucose monitoring"
]

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

result = {}
keyword_list =[]
link_list = []
source_list = []
title_list = []

for keyword in keywords_prod:
    driver.get('https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en')
    time.sleep(3)

    search_box = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]')
    # string 수정
    string = str(keyword)
    search_box.send_keys(string + ' when:1d')
    search_box.send_keys(Keys.RETURN)

    # link
    get_url = driver.current_url
    page = requests.get(get_url)
    soup = bs(page.text, "html.parser")

    elements = soup.find_all("a", "VDXfz")
    # source 
    elements_source = soup.find_all("a", "wEwyrc")
    sources = []
    for i in elements_source:
        sources.append(i.get_text())
    if len(elements)==0:
        continue

    # title
    elements_title = soup.find_all("a", "RZIKme")
    print(elements_title)
    titles = []
    for title in elements_title:
        titles.append(title.get_text())

        
    for i in range(len(elements)):
        plus_link = str(elements[i]).split('"')[5].split(".")[1]
        new_link = 'https://news.google.com' + plus_link

        if new_link in link_list:
            continue
        check_title = titles[i].upper().split()
        if str("CMA") in check_title:
            continue

        keyword_list.append(keyword)
        link_list.append(new_link)
        source_list.append(sources[i])
        title_list.append(titles[i])


for keyword in keywords_tech:
    driver.get('https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en')
    time.sleep(3)

    search_box = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]')
    # string 수정
    string = str(keyword)
    search_box.send_keys(string + ' when:1d')
    search_box.send_keys(Keys.RETURN)

    #link
    get_url = driver.current_url
    page = requests.get(get_url)
    soup = bs(page.text, "html.parser")

    elements = soup.find_all("a", "VDXfz")
    #source 
    elements_source = soup.find_all("a", "wEwyrc")
    sources = []
    for i in elements_source:
        sources.append(i.get_text())
    if len(elements)==0:
        continue

    #title
    elements_title = soup.find_all("a", "RZIKme")
    print(elements_title)
    titles = []
    for title in elements_title:
        titles.append(title.get_text())


    for i in range(len(elements)):
        plus_link = str(elements[i]).split('"')[5].split(".")[1]
        new_link = 'https://news.google.com' + plus_link

        if new_link in link_list:
            continue
        check_title = titles[i].upper().split()
        if str("CMA") in check_title:
            continue

        keyword_list.append(keyword)
        link_list.append(new_link)
        source_list.append(sources[i])
        title_list.append(titles[i])



for keyword in keywords_policy:
    driver.get('https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en')
    time.sleep(3)

    search_box = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]')
    # string 수정
    string = str(keyword)
    search_box.send_keys(string + ' when:1d')
    search_box.send_keys(Keys.RETURN)

    #link
    get_url = driver.current_url
    page = requests.get(get_url)
    soup = bs(page.text, "html.parser")

    elements = soup.find_all("a", "VDXfz")
    #source 
    elements_source = soup.find_all("a", "wEwyrc")
    sources = []
    for i in elements_source:
        sources.append(i.get_text())
    if len(elements)==0:
        continue

    #title
    elements_title = soup.find_all("a", "RZIKme")
    print(elements_title)
    titles = []
    for title in elements_title:
        titles.append(title.get_text())

    for i in range(len(elements)):
        plus_link = str(elements[i]).split('"')[5].split(".")[1]
        new_link = 'https://news.google.com' + plus_link

        if new_link in link_list:
            continue
        check_title = titles[i].upper().split()
        if str("CMA") in check_title:
            continue

        keyword_list.append(keyword)
        link_list.append(new_link)
        source_list.append(sources[i])
        title_list.append(titles[i])


result["keyword"] = keyword_list
result["title"] = title_list
result["source"] = source_list
result["link"] = link_list

index = [i for i in range(len(keyword_list))]
result = pd.DataFrame(result, index=index)
now = datetime.now()
date = str(now.strftime("%Y%m%d"))
filename = 'C:/Users/BRAIN/(주)에이치엠이스퀘어/한윤진 - 한윤진-업무_공유/5 마케팅/뉴스 크롤링/' + str(date)+'_US.xlsx'
result.to_excel(filename, index=False)

# google translate
from googletrans import Translator
translator = Translator()

translate_list = []
for t in title_list:
    result = translator.translate(t, src='en', dest='ja')
    result = translator.translate(result.text, src='ja', dest='ko')
    print(result.text)
    translate_list.append(result.text)

import openpyxl
NEWS = openpyxl.load_workbook(filename)
NEWS_S = NEWS.active

for cell in NEWS_S["D"]:
    if cell.value == "link":
        continue
    cell.hyperlink = cell.value
    cell.value = "LINK"
    cell.style = "Hyperlink"

NEWS_S.freeze_panes = "B2"
NEWS_S.title = 'EN'

NEWS.copy_worksheet(NEWS_S)
NEWS_S = NEWS["EN Copy"]
x = 0
for cell in NEWS_S["B"]:
    if cell.value == "title":
        continue
    cell.value = translate_list[x]
    x += 1

NEWS_S.freeze_panes = "B2"
NEWS_S.title = 'KR'

NEWS.save(filename)





