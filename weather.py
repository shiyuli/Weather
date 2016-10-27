# -*- coding: utf-8 -*-
import urllib2
import json

where = {}
with open("where.txt", "rb") as f:
	while True:
		txt = f.readline()
		if not txt:
			break
		
		key = txt[10:][:-2]
		value = txt[0:9]
		where[key] = value
	f.close()
#print where
txt = raw_input('Please input a place:\n')
result = where[txt.decode('gbk').encode('utf-8')]
#print "The weather in\t" + result
url = 'http://www.weather.com.cn/data/sk/' + result + '.html'
weatherHTML = urllib2.urlopen(url).read()
weatherJSON = json.JSONDecoder().decode(weatherHTML)
weatherInfo = weatherJSON['weatherinfo']

print weatherInfo
print u'城市:\t', weatherInfo['city']
print u'风向:\t', weatherInfo['WD']
print u'风级:\t', weatherInfo['WSE']
print u'温度:\t', weatherInfo['temp'] + u'摄氏度'
print 'njd:\t', weatherInfo['njd']
print 'qy:\t', weatherInfo['qy']
print u'雷达:\t', weatherInfo['isRadar']
print 'rain:\t', weatherInfo['rain']
print 'cityid:\t', weatherInfo['cityid']
print 'Radar:\t', weatherInfo['Radar']
print 'WS:\t', weatherInfo['WS']
print 'time:\t', weatherInfo['time']
print 'SD:\t', weatherInfo['SD']
