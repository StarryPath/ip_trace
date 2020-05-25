import os,sys,time,subprocess
from scapy.as_resolvers import AS_resolver_radb
import pymysql
db = pymysql.connect("localhost", "root", "root", "bishe")
cursor = db.cursor()

sql = "select lon,lat from bd_locip where ip='"+"1.1.1.1"+"'"
cursor.execute(sql)
long=cursor.fetchall()[0][0]
lat=cursor.fetchall()[0][1]
