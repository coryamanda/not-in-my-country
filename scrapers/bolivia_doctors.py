# Import modules
import urllib2
from bs4 import BeautifulSoup

# Declarations
HOMEPAGE = 'http://www.colmedlapaz.org/index.php?option=com_wrapper&view=wrapper&Itemid=72'

# Read webpage
html = urllib2.urlopen(HOMEPAGE).read()
html = BeautifulSoup(html)
soup.prettify()
for anchor in soup.findAll('a', href=True):
    print anchor['href']