from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import time
import requests
import re

url = "https://parking.klcc.com.my/"

def timestamp():
	timestamp = ''
	for i in content.findAll('h3'):
		timestamp = timestamp + ' ' + i.text
		ts = timestamp.split(" ")[4]+" "+ timestamp.split(" ")[5]
	print(ts)

def parking_name():
	parking =  []
	for i in content.findAll('h4'):
		p = i.text
		print(p)
		parking.append(p)
	#print(parking)

def total():
	#read from linux command also can
	#value = os.popen("curl -s https://parking.klcc.com.my/ | grep -w 'value' | grep -v 'text'| sed 's/[^0-9]*//g'").read()
	value = requests.get("https://parking.klcc.com.my/")
	value_lines = value.text.splitlines()
	value_array = []

	for line in value_lines:
		if re.findall("value", line) and not re.findall("text", line):
			if not re.findall("valueStrokeClass", line):
				value_array.append(re.findall("([0-9]+)", line)[0])
	#print(value_array)
	
	for tt in range(len(value_array)):
		print(value_array[tt])
	return 0

try:
	while True:
		print("\nThis App will keep refreshing in 15 seconds:")
		print("Kindly press ctrl + z to terminate the program\n")

		page = urlopen(url)
		soup = BeautifulSoup(page, 'html.parser')
		content = soup.find('div', {"class": "contentgray"})

		#calling functions
		timestamp()
		parking_name()
		total()
		time.sleep(15)

except KeyboardInterrupt:
	print("System Exitting")
