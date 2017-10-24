# Exit status 1 - Internet Connection or URL Problem

import requests,bs4,re,sys,os
import time
from time import *

#provide first url
url=sys.argv[1]
temp_words = url[30:].split('%20')
name_of_the_anime = ""
for word in temp_words:
	name_of_the_anime += word


mainsite="http://animeheaven.eu/"

destination=sys.argv[2]
starting_ep = sys.argv[3]
ending_ep = sys.argv[4]
r=""

try:
	r=requests.get(url)
	r.raise_for_status()
except:
	print("Error")
	sys.exit(1)


if not os.path.exists(os.path.dirname(destination)):
	os.makedirs(os.path.dirname(destination))

soup=bs4.BeautifulSoup(r.text,"html.parser")

dpages=soup.select(".infoepbox > a")
#print(dpages)
#now iterate over all episode pages
print("-----------we are downloading "+name_of_the_anime+"from "+starting_ep +" to "+ending_ep+"-----------------------------")
for i in range(len(dpages)-1,-1,-1):

	if (len(dpages)-i) >= int(starting_ep) and (len(dpages)-i) <= int(ending_ep):

		print("Downloading Episode "+str(len(dpages)-i)+".mp4 of "+name_of_the_anime)
		r2=requests.get(mainsite+dpages[i].get("href"))

		try:
			r2.raise_for_status()
		except:
			print("Error")
			continue;


		soup2=bs4.BeautifulSoup(r2.text,"html.parser")

		dlink=soup2.select("script")
		#print(dlink[4])
		#the 5th script contains my link

		mylink=re.compile(r"href='(.*)'")
		downlink=mylink.search(str(dlink[4]))[1][:-17]
		print("Here it is",downlink+"   "+ str(type(downlink)))
	    
		t = strftime("%a, %d %b %Y %H:%M:%S", localtime())
		print(t)

		downloaded=requests.get(downlink)

		print("downloaded requests works !!  ----------------")

		try:
			downloaded.raise_for_status()
		except:
			print("Error")
			continue;

		with open(name_of_the_anime+"Episode "+str(len(dpages)-i)+".mp4","wb") as f:
			for con in downloaded.iter_content(100000):
				f.write(con)

		print("Downloaded Episode "+str(len(dpages)-i)+".mp4")
		f.close()

	else:
		continue

	'''
	http://animeheaven.eu/i.php?a=My%20Wife%20Is%20the%20Student%20Council%20President
	'''
	
	#f_name = name_of_anime+"E"+str(len(dpages)-i)+".mp4"
	#curl(downlink) --output "f_name"
