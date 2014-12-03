import urllib2
import json

url = 'http://dev.c0l.in:8888'
api = urllib2.urlopen(url)
data = json.load(api)

for item in data:
    print item['sector'], item['company']['purchases']
