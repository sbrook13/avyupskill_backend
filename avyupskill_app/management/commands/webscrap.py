import bs4 as bs
import re
import urllib.request
from bs4 import BeautifulSoup

import requests
from datetime import datetime, date
from django.core.management.base import BaseCommand
from ...models import Course

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
  ssl._create_default_https_context = ssl._create_unverified_context

courses_all = 'https://aiare.info/course_list.php?criteria=co&type=av'
course_page1 = 'https://aiare.info/course_list.php?page=1&skip=0&max=100&sort=dateBegin&criteria=co'
course_page2 = 'https://aiare.info/course_list.php?page=2&skip=100&max=100&sort=dateBegin&criteria=co'
course_page3 = 'https://aiare.info/course_list.php?page=3&skip=200&max=100&sort=dateBegin&criteria=co'
course_page4 = 'https://aiare.info/course_list.php?page=4&skip=300&max=100&sort=dateBegin&criteria=co'
detail_base_url = 'https://aiare.info/'

page_html = urllib.request.urlopen(courses_all).read()

# HTML Parsing
soup = BeautifulSoup(page_html, 'html.parser')

allCourses = []
allRows = soup.find_all('tr')
for row in allRows:
  dataRow = []
  row_list = row.find_all('td')
  for cell in row_list[1:]:
    dataRow.append(cell.text)
  link = row.find("a")['href']
  detail_url = detail_base_url + link
  dataRow.append(detail_url)
  detail_html = urllib.request.urlopen(detail_url).read()
  detail_soup = BeautifulSoup(detail_html, 'html.parser')
  class_details = detail_soup.find_all('p',{ "class" : "dataindent" })
  for detail in class_details:
    dataRow.append(detail.text)
  allCourses.append(dataRow)
titles = allCourses[0]
allCourses = allCourses[1:]

def seed_courses():
  for i in allCourses:
    start = get_date(i[2])
    if i[3] == "" :
      end = start
    else: 
      end = get_date(i[3])
    course = Course(
      class_type=i[0],
      provider=i[1],
      start_date= start,
      end_date=end,
      location=i[4],
      details_url=i[6],
      aiare_url=i[7],
      provider_url=i[8],
      phone=i[9],
      contact_email=i[10],
      cost=i[14],
    )
    course.save()

def get_date(date):
  newDate = datetime.strptime(date, "%m/%d/%Y").strftime("%Y-%m-%d")
  return(newDate)

def clear_data():
  Course.objects.all().delete()

class Command(BaseCommand):
  def handle(self, *args, **options):
    clear_data()
    seed_courses()
    print("completed course seeds")
    
# EXAMPLE COURSE FROM BS4
# [0]  'AIARE 1 ', 
# [1]  'Apex Mountain School', 
# [2]  '11/17/2020', 
# [3]  '11/22/2020', 
# [4]  'Vail', 
# [5]  'CO']
# [6]  'https://aiare.info/course_detail.php?recid=9303', 
# [7]  'http://avtraining.org/aiare-level-1/', 
# [8]  'apexmountainschool.com/', 
# [9]  '(970) 949-9111 (Wk)', 
# [10]  'ski@apexmountainschool.com', 
# [11]  ''
# [12]  'Vail, CO', 
# [13]  'Begin: 11/17/2020; End: 11/22/2020', 
# [14]  '$565',
# [15]  '' 
