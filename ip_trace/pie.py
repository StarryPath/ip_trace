import pymysql
import json
# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "bishe")
cursor = db.cursor()
sql = "select tra from trace"
cursor.execute(sql)
cnt_ip=set()
cnt_x=0
for trace in cursor.fetchall():
    trace_ip = trace[0].split()
    for ip in trace_ip:
        if ip[0]=="*":
            cnt_x+=1
        else:
            cnt_ip.add(ip)
print(cnt_x)
print(len(cnt_ip))
sql = "select tra2 from nm2"
cursor.execute(sql)
cnt_ip2=set()
cntx2=set()
for trace in cursor.fetchall():
    trace_ip = trace[0].split()
    for ip in trace_ip:
        if ip[0]=="*":
            cntx2.add(ip[1:])
        else:
            cnt_ip2.add(ip)
print(len(cntx2))
print(len(cnt_ip2))

sql = "select tra3 from nm3"
cursor.execute(sql)
cnt_ip3=set()
cntx3=set()
for trace in cursor.fetchall():
    trace_ip = trace[0].split()
    for ip in trace_ip:
        if ip[0]=="*":
            cntx3.add(ip[1:])
        else:
            cnt_ip3.add(ip)
print(len(cntx3))
print(len(cnt_ip3))

sql = "select tra from final_trace"
cursor.execute(sql)
cnt_ip4=set()
cntx4=set()
for trace in cursor.fetchall():
    trace_ip = trace[0].split()
    for ip in trace_ip:
        if ip[0]=="*":
            cntx4.add(ip[1:])
        elif ip[0]=='a':
            continue

        else:
            cnt_ip4.add(ip)
print(len(cntx4))
print(len(cnt_ip4))
