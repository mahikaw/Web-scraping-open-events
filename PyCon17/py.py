import urllib2
import json
from bs4 import BeautifulSoup
url="https://us.pycon.org/2017/schedule/sponsor-tutorials/list/"
page=urllib2.urlopen(url)
soup=BeautifulSoup(page)
lists=[]
divs=soup.find_all("div",{'class':'box-content'})
for div in divs:
	for i in range(0,len(div.find_all("a"))):
		dictionary={}
		dictionary['id']=i+132
		dictionary['speakers']=[]
		dictionary['subtitle']=""
		dictionary['short_abstract']=""
		dictionary['session_type']={}
		dictionary['start_time']=""
		dictionary['end_time']=""
		dictionary['track']={"color": "#F39C12","font_color": "#000000","id": 3,"name": "Sponsor tutorials"}
		dictionary['comments']= ""
		dictionary['language']="English"
		dictionary['slides']=""
		dictionary['audio']=""
		dictionary['video']=""
		dictionary["level"]=""
		dictionary["signup_url"]=""
		dictionary['state']="accepted"
		dictionary['microlocation']={}
		dictionary['title']=div.find_all("a")[i].string
		string_details=str(div.find_all("p")[i])
		formatted_details=string_details.replace("<br>","").replace("<b>","").replace("<p>","").replace("</p","").replace("</b>","").replace("\n","").replace("<br/>","")
		dictionary['details']=formatted_details
		dictionary['long_abstract']=div.find_all("div")[i].string
		lists.append(dictionary)
print json.dumps(lists)
