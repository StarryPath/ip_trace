import json
import pymysql
db = pymysql.connect("localhost", "root", "root", "bishe")
cursor = db.cursor()
sql = "select tra from trace limit 100"
cursor.execute(sql)
myTree={}
for trace in cursor.fetchall():
    trace_ip = trace[0].split()
    #print(trace_ip)
    for i in range(len(trace_ip)):
        if i!=len(trace_ip)-1:
            if trace_ip[i] not in myTree:
                myTree[trace_ip[i]]=set()
                myTree[trace_ip[i]].add(trace_ip[i + 1])
            else:
                myTree[trace_ip[i]].add(trace_ip[i+1])
            print(trace_ip[i+1])
print(myTree)
tree={}

