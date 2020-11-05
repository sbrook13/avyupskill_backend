import bs4 as bs
import urllib.request
from bs4 import BeautifulSoup

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
  ssl._create_default_https_context = ssl._create_unverified_context

course_url = 'https://aiare.info/course_detail.php?recid=9302'
# https://aiare.info/course_list.php?sort=dateBegin&criteria=co'
page_html = urllib.request.urlopen(course_url).read()

# HTML Parsing
page_soup = BeautifulSoup(page_html, 'html.parser')

print(page_soup)



# <tr>
#   <td class="linkCell">
#     <a 
#       href="course_detail.php?recid=9302" 
#       title="Click for course detail."
#     >
#       detail
#     </a>
#   </td>
#   <td>
#     <a href="course_detail.php?recid=9302 ">
#       AIARE 1 
#     </a>
#   </td>
#   <td>Apex Mountain School</td>
#   <td>11/10/2020</td>
#   <td>11/15/2020</td>
#   <td>Vail</td>
#   <td>CO</td>
# </tr>
