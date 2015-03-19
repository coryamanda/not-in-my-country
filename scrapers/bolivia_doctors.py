# Import modules
import urllib2
from bs4 import BeautifulSoup

# Declarations
HOMEPAGE = 'http://www.colmedlapaz.org/index.php?option=com_wrapper&view=wrapper&Itemid=72'

# Pull HTML
html = urllib2.urlopen(HOMEPAGE).read()

# Transform HTML
soup = BeautifulSoup(html)

# TODO: FIND A WAY TO NAVIGATE THE DROPDOWN MENU "Especialidad:"