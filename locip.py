#!/usr/bin/python
#-*-coding:utf-8-*-
import urllib.request
import json
trace_ips="47.94.90.222"
url="http://api.map.baidu.com/location/ip?ak=03jNFtRzoo6OTFGdG6oyzhpkSN8LohwX&ip="+trace_ips+"&coor=bd09ll"
html = urllib.request.urlopen(url)
hjson=json.loads(html.read())
print(hjson["address"])
print(hjson["content"])
print(hjson["content"]["point"])
print(hjson["content"]["point"]["x"])
print(hjson["content"]["point"]["y"])