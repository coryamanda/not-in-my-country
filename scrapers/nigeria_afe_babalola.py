from bs4 import BeautifulSoup
import re
import urllib2

#doc = urllib2.urlopen("http://abuad.edu.ng.cp-38.webhostbox.net/en/academics/staff-profile.html")
#rawdata = ''.join(doc)
#open("data.txt","w+").write(rawdata)

doc = open("data.txt").read()

soup = BeautifulSoup(''.join(doc))
for department in soup.find_all("div",{"class":"wf_department_details"}):
    name = department.find_all("h3",{"class":"wf_department_name"})
    name = name[0].text
    num = int(name.split("(")[1].split(")")[0])
    name = name.split("(")[0].strip()
    #print "Department:", name,num

    for link in list(department.find_all_next("a"))[:num+1]: 
        if 'employee' in link.get("href"):
            title = str(link.find_next().text.strip())
            try:
                title = title.split("-")[1].strip()
            except:
                continue
            print ",".join([name, link.text, title])
