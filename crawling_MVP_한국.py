import selenium
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import time, requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from notion.client import NotionClient


keywords_prod_kr = [
    "애보트 프리스타일리브레",
    "덱스콤 G6", "덱스콤 G7",
    "메드트로닉 가디언 센서", "삼성 혈당", 
    "동원아나텍 D-salife"
]

keywords_tech_kr = [
    "연속혈당측정기", "연속혈당모니터링", 
    "광음향 혈당", "광음향 포도당", "광음향 의료기기",
    "비침습 혈당", "비침습 포도당",
    "스마트워치 혈당", "스마트워치 포도당",
    "웨어러블 혈당", "웨어러블 포도당"
]

keywords_policy_kr = [
    "당뇨병 의료보험", "당뇨병 건강보험", "당뇨병 헬스케어",
    "FDA 당뇨병", "FDA 혈당", "FDA 포도당", "FDA 연속혈당측정기", "FDA 혈당측정기", "FDA 혈당 모니터링",
    "임상연구 연속혈당측정기", "임상연구 혈당측정기", "임상연구 혈당 모니터링",
    "임상시험 CGM", "임상시험 혈당 측정기", "임상시험 혈당 모니터링"
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

for keyword in keywords_prod_kr:
    driver.get('https://news.google.com/topstories?hl=ko&gl=KR&ceid=KR:ko')
    time.sleep(5)

    search_box = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]')
    # string 수정
    string = str(keyword)
    search_box.send_keys(string + ' when:5d')
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

for keyword in keywords_tech_kr:
    driver.get('https://news.google.com/topstories?hl=ko&gl=KR&ceid=KR:ko')
    time.sleep(5)

    search_box = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]')
    # string 수정
    string = str(keyword)
    search_box.send_keys(string + ' when:5d')
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

for keyword in keywords_policy_kr:
    driver.get('https://news.google.com/topstories?hl=ko&gl=KR&ceid=KR:ko')
    time.sleep(5)

    search_box = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]')
    # string 수정
    string = str(keyword)
    search_box.send_keys(string + ' when:5d')
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
filename = 'C:/Users/BRAIN/(주)에이치엠이스퀘어/한윤진 - 한윤진-업무_공유/5 마케팅/뉴스 크롤링/' + str(date)+'_KR.xlsx'
result.to_excel(filename, index=False)

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
NEWS.save(filename)