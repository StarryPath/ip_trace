import pymysql


db = pymysql.connect("localhost", "root", "root", "bishe")
cursor=db.cursor()
sql="select tra from trace"
cursor.execute(sql)
trace_all=[]
for trace in cursor.fetchall():
    print(trace[0])
    trace_ip=trace[0].split()
    trace_all.append(trace_ip)
