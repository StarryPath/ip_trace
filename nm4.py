import pymysql
db = pymysql.connect("localhost", "root", "root", "bishe")
cursor = db.cursor()
sql = "select tra3 from nm3 "
cursor.execute(sql)
nm_dict={}
cnt=0
anstra=[]
#[上一跳,下一跳,跳数]
for trace in cursor.fetchall():
    trace_ip = trace[0].split()
    for i in range(len(trace_ip)):
        if trace_ip[i][0]=='*':
            if trace_ip[i+1][0]=='*':
                cnt+=1
                pairs=(trace_ip[i-1],'*')
                if pairs not in nm_dict:
                    nm_dict[pairs]=trace_ip[i]
                else:
                    trace_ip[i]=nm_dict[pairs]
    anstra.append(trace_ip)
print(anstra)
cnt_ip3=set()
cntx3=set()
for tra in anstra:
    str=""
    for t in tra:
        if t[0] == "*":
            cntx3.add(t[1:])
        else:
            cnt_ip3.add(t)
print(len(cntx3))
print(len(cnt_ip3))
