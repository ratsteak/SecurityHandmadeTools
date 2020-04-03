import requests
import sys

try:
	d = requests.get(str(sys.argv[1]))
	f = open(str(sys.argv[1]).split("://")[1], 'wb')
	f.write(d.content)
except:
	print(sys.exc_info()[0])
	print("Usage: python wget.py fullurl")



