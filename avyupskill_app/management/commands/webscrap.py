import bs4 as bs
import re
import urllib.request
from bs4 import BeautifulSoup

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
  ssl._create_default_https_context = ssl._create_unverified_context

course_url = 'https://aiare.info/course_list.php?sort=dateBegin&criteria=co'
detail_base_url = 'https://aiare.info/'

page_html = urllib.request.urlopen(course_url).read()

# HTML Parsing
soup = BeautifulSoup(page_html, 'html.parser')

allCourses = []
allRows = soup.find_all('tr')
for row in allRows:
  dataRow = []
  link = row.find("a")['href']
  detail_url = detail_base_url + link
  dataRow.append(detail_url)
  detail_html = urllib.request.urlopen(detail_url).read()
  detail_soup = BeautifulSoup(detail_html, 'html.parser')
  class_data = detail_soup.find_all('p',{ "class" : "dataindent" }, text=True)
  for detail_row in class_data:
    dataRow.append(detail_row.text)
  row_list = row.find_all('td')
  for cell in row_list[1:]:
    dataRow.append(cell.text)
  allCourses.append(dataRow)
titles = allCourses[0]
allCourses = allCourses[1:]

def seed_courses():
  for i in allCourses:
  course = Course(
    details_url=i[0],
    aiare_url=i[1],
    provider_url=i[2],
    phone=i[3],
    location=i[4],
    cost=i[6],
    class_type=i[7],
    provider=i[8],
    start_date=i[9],
    end_date=i[10]
  )
    
# EXAMPLE COURSE FROM BS4
# ['https://aiare.info/course_detail.php?recid=9303', 
# 'http://avtraining.org/aiare-level-1/', 
# 'apexmountainschool.com/', 
# '(970) 949-9111 (Wk)', 
# 'ski@apexmountainschool.com', 
# 'Vail, CO', 
# 'Begin: 11/17/2020; End: 11/22/2020', 
# '$565', 
# 'AIARE 1 ', 
# 'Apex Mountain School', 
# '11/17/2020', 
# '11/22/2020', 
# 'Vail', 
# 'CO']