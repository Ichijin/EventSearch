import requests
import os
import sys
from bs4 import BeautifulSoup
from serpapi import GoogleSearch

search = GoogleSearch({
    'q':'イベント',
    'engine':'google',
    'location':'Tokyo, Tokyo, Japan',
    'api_key':'a8748b594144dc7e9f7037efa045631afca5911081ac7841da89b10836255584'
    })

results = search.get_dict()

for result in results['organic_results']:
    print(result['title']+' url:'+result['link'])

    url = result['link']
    if 'gotokyo' in url:
        url = 'https://www.gotokyo.org/ja/travel-directory/result/index/event_date_word/today'
        
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    hrefs = []
    titles = []
    periods = []
    if 'walkerplus' in html:
        hrefs = soup.select('div.m-mainlist-item > a')
        periods = soup.select('p.m-mainlist-item-event__period')
        for i in range(len(hrefs)):
            print(hrefs[i])
            if i < len(periods):
                print(periods[i].text)
    elif 'enjoytokyo' in html:
        hrefs = soup.select('.article-link')
        titles = soup.select('.article-list_vertical-item-text')
        periods = soup.select('ul.event-info-list > li._date')
        for i in range(len(hrefs)):
            print(hrefs[i])
            print(titles[i].text)
            if i < len(periods):
                print(periods[i].text)
    elif 'jalan' in html:
        hrefs = soup.select('p.item-name > a')
        periods = soup.select('dl.item-eventInfo > dd')
        for i in range(len(hrefs)):
            print(hrefs[i])
            if i < len(periods):
                print(periods[i].text)
    elif 'osotoiko' in html:
        hrefs = soup.select('p.item-title_arcv2 > a')
        periods_s = soup.select('div.date-eventstart > span.fa-flag')
        periods_e = soup.select('div.date-ouchitoday > span.fa-cal')
        for i in range(len(hrefs)):
            print(hrefs[i])
            if i < len(periods_s):
                print(periods_s[i].text)
            if i < len(periods_e):
                print(periods_e[i].text)
    elif 'gotokyo' in html:
        hrefs = soup.select('li.result_lists_li > a')
        titles = soup.select('div.c-stuffing--xs')
        periods = soup.select('div.result_image > span.result_date')
        for i in range(len(hrefs)):
            print(hrefs[i])
            if i < len(titles):
                print(titles[i].text)
            if i < len(periods):
                print(periods[i].text)
    elif 'https://iko-yo' in html:
        hrefs = soup.select('div.c-grid__header--orange > a')
        titles = soup.select('div.c-grid__header--orange > h3.c-grid__title')
        periods = soup.select('div.c-grid__content > div.c-container--xs')
        for i in range(len(hrefs)):
            print(hrefs[i].text)
            if i < len(titles):
                print(titles[i].text)
            if i < len(periods):
                print(periods[i].text)
