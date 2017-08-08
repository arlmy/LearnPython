# -*- coding: utf-8 -*-

import urllib.request
import re
from bs4 import BeautifulSoup
import pickle

response = urllib.request.urlopen('http://www.baidu.com/s?wd=%E9%92%9B')
html_doc = response.read()
soup = BeautifulSoup(html_doc, "html.parser")
body = soup.find("body")

output1 = open('description.txt', 'wb')
output2 = open('keywords.txt', 'wb')

for link in body.find_all("a", class_="c-showurl"):
    first_link = link.get("href")
#    print(link.get("href"))
    response = urllib.request.urlopen(first_link)
    print(response.geturl())
    re_response = urllib.request.urlopen(response.geturl())
    first_link_html = re_response.read()
    first_link_soup = BeautifulSoup(first_link_html, "html.parser")
    print(first_link_soup.find('meta', attrs = {'name':'description'})['content'])
    pickle.dump(first_link_soup.find('meta', attrs = {'name':'description'})['content'], output1)
    print(first_link_soup.find('meta', attrs = {'name':'keywords'})['content'])
    pickle.dump(first_link_soup.find('meta', attrs = {'name':'keywords'})['content'], output2)

#response = urllib.request.urlopen(first_link)
#re_response = urllib.request.urlopen(response.geturl())
#first_link_html = re_response.read()
#first_link_soup = BeautifulSoup(first_link_html, "html.parser")
#print(first_link_soup.find('meta', attrs = {'name':'description'})['content'])
#print(first_link_soup.find('meta', attrs = {'name':'keywords'})['content'])
