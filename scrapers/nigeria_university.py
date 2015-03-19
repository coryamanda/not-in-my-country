import urllib2

from bs4 import BeautifulSoup

response = urllib2.urlopen('http://unn.edu.ng/academics/faculties')
html_doc = response.read()
soup = BeautifulSoup(html_doc)
departments = soup.find_all()

print soup

<a href="http://unn.edu.ng/department/faculty-social-sciences-staff-list" target="_blank">Faculty Staff</a>