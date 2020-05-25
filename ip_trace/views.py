from django.shortcuts import render
import pymysql
from scapy.all import *
from django.http import HttpResponse
from .forms import trace_ip
import geoip2.database
import urllib.request
import json
reader = geoip2.database.Reader("/home/fy/trace_show/ip_trace/static/GeoLite2-City.mmdb")
def raw(request):
    db = pymysql.connect("localhost", "root", "root", "bishe")
    cursor=db.cursor()
    sql="select tra from trace limit 200"
    cursor.execute(sql)
    ip_all=[]
    dian_set=set()
    nm_set=set()
    for trace in cursor.fetchall():
        trace_ip=trace[0].split()
        ip_line=[]
        lon1 = 0
        lan1 = 0
        lon2 = 0
        lan2 = 0
        for i in range(len(trace_ip)):
            if trace_ip[i][0]!='*':
                try:
                    response = reader.city(trace_ip[i])

                    if lon2==0:
                        lon1=response.location.longitude
                        lan1=response.location.latitude
                    else:
                        lon1 = response.location.longitude
                        lan1 = response.location.latitude
                        lon=(lon1+lon2)*0.5
                        lan=(lan1+lan2)*0.5
                        if lon1!=lon2:
                            ip_line.append((lon,lan))

                            nm_set.add((lon,lan))
                        print(lon1,lon2,lon)
                        lon2=0
                        lan2=0
                    ip_line.append((response.location.longitude, response.location.latitude))
                    dian_set.add((response.location.longitude, response.location.latitude))
                except Exception as e:
                    print(e)
            else:
                if lon1!=0:
                    lon2=lon1
                    lan2=lan1
        ip_all.append(ip_line)
        #trace_all.append(trace_ip)

    return render(request, 'raw_pic.html',{'ip_all':ip_all,'dian_set':dian_set,'nm_set':nm_set})
# Create your views here.
def logic(request):
    return render(request, 'logic.html')
def pie(request):
    return render(request, 'pie.html')
def alias(request):
    return render(request,'alias.html')
def tree(request):
    return render(request,'tree.html')
def nm(request):
    return render(request,'nm.html')
def index(request):
    return render(request,'index.html')
def trace(request):
    if request.method == 'POST':  # 当提交表单时

        form = trace_ip(request.POST)  # form 包含提交的数据


        ip = form.data['ip']
        ans, unans = traceroute(ip, timeout=5)
        ip_list = []
        for snd, rcv in ans:
            ip_list.append((snd.ttl, rcv.src))
        ip_list.sort(key=lambda x: x[0])
        s=""
        i=1
        for a in ip_list:
            try:
                response = reader.city(a[1])
            except Exception as e:
                print(e)
            # print(a[1])
            while i < a[0]:
                # print(i,snd.ttl)
                s = s + '*'
                s += ' '
                i = i + 1
            if i != 1:
                s += a[1]
                s += ' '

                if ip == a[1]:

                    break
            i = i + 1
        print(s)
        trace_ips = s.split()
        ip_line = []
        lon1 = 0
        lan1 = 0
        lon2 = 0
        lan2 = 0
        ip_all = []
        dian_set = {}
        nm_set = set()
        db = pymysql.connect("localhost", "root", "root", "bishe")
        cursor = db.cursor()
        for i in range(len(trace_ips)):
            if trace_ips[i] != '*':
                try:
                    sql = "select lon,lat from bd_locip where ip='"+trace_ips[i]+"'"
                    cursor.execute(sql)
                    long=float(cursor.fetchall()[0][0])
                    lat=float(cursor.fetchall()[0][1])
                except:
                    try:
                        url="http://api.map.baidu.com/location/ip?ak=03jNFtRzoo6OTFGdG6oyzhpkSN8LohwX&ip="+trace_ips[i]+"&coor=bd09ll"
                        html = urllib.request.urlopen(url)
                        hjson = json.loads(html.read())
                        long=float(hjson["content"]["point"]["x"])
                        lat=float(hjson["content"]["point"]["y"])
                        sql="INSERT INTO bd_locip(ip,lat, lon) VALUES ('%s','%s','%s')" % (ip, lat, long)
                        try:
                            # 执行sql语句
                            cursor.execute(sql)
                            # 提交到数据库执行
                            db.commit()
                        except Exception as c:
                            # 如果发生错误则回滚
                            print(c)
                            db.rollback()
                    except Exception as c:
                            continue

                if lon2 == 0:
                    lon1 = long
                    lan1 = lat
                else:
                    lon1 = long
                    lan1 = lat
                    lon = (lon1 + lon2) * 0.5
                    lan = (lan1 + lan2) * 0.5
                    if lon1 != lon2:
                        if (len(ip_line)==0)or(ip_line[-1]!=(lon, lan)):
                            ip_line.append((lon, lan))

                        nm_set.add((lon, lan))
                    print(lon1, lon2, lon)
                    lon2 = 0
                    lan2 = 0
                if (len(ip_line)==0)or(ip_line[-1] != (long, lat)):
                    ip_line.append((long,lat))
                if (long,lat) not in dian_set:
                    dian_set[(long,lat)]=""
                    dian_set[(long,lat)]+=str(trace_ips[i])
                    dian_set[(long, lat)] +="  "
                else:
                    dian_set[(long, lat)] += str(trace_ips[i])
                    dian_set[(long, lat)] += "  "

            else:
                if lon1 != 0:
                    lon2 = lon1
                    lan2 = lan1
        ip_all.append(ip_line)
        return render(request, 'move_trace.html', {'ip_all':ip_all,'dian_set':dian_set,'nm_set':nm_set})

    else:  # 当正常访问时
        form = trace_ip()
        return render(request, 'trace.html', {'form': form})