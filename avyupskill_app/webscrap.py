import bs4 as bs
import urllib.request
from bs4 import BeautifulSoup

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
ssl._create_default_https_context = ssl._create_unverified_context

course_url = 'https://aiare.info/course_list.php?sort=dateBegin&criteria=co'
page_html = urllib.request.urlopen(course_url).read()
uClient.close()

# HTML Parsing
page_soup = BeautifulSoup(page_html, 'html.parser')

print(page_soup.title)

print(page_soup.h1)