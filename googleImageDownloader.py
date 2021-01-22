import requests
from bs4 import BeautifulSoup
import urllib.request
import os

def downloadImage(query, fileLocation, n=4):
	URL = "https://www.google.com/search?tbm=isch&q=" + query
	result = requests.get(URL)
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')
	imgTags = soup.find_all('img', class_='t0fcAb')

	count=0
	for i in imgTags:
		if count==n: break
		try:
			urllib.request.urlretrieve(i['src'], f'{fileLocation}/' + str(count) + '.jpg')
			count+=1
			print('Downloaded', count)
		except Exception as e:
			raise e
      
      
downloadImage("India", "C:\Users\Roshan\Desktop", 10) #10 images will be downloaded 
