from django.shortcuts import render
import pymysql
from django.http import HttpResponse
import geoip2.database
reader = geoip2.database.Reader("/home/fy/trace_show/ip_trace/static/GeoLite2-City.mmdb")
def raw(request):
    db = pymysql.connect("localhost", "root", "root", "bishe")
    cursor=db.cursor()
    sql="select tra from trace"
    cursor.execute(sql)
    ip_all=[]
    dian_set=set()
    for trace in cursor.fetchall():
        trace_ip=trace[0].split()
        ip_line=[]
        for ip in trace_ip:
            if ip!='*':
                try:
                    response = reader.city(ip)
                    ip_line.append(( response.location.longitude,response.location.latitude))
                    dian_set.add(( response.location.longitude,response.location.latitude))
                except Exception as e:
                    print(e)
        ip_all.append(ip_line)
        #trace_all.append(trace_ip)
    return render(request, 'raw_pic.html',{'ip_all':ip_all,'dian_set':dian_set})
# Create your views here.
def logic(request):
    return render(request, 'logic.html')