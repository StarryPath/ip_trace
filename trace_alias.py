import pymysql
import json
# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "bishe")

# 使用cursor()方法获取操作游标
cursor = db.cursor()
ali={}
file = open("kapar.aliases")
i=1
cnt=1
rootschild=[]
while True:
    line = file.readline()  # 只读取一行内容
    line = line.strip('\n')
    if not line:
        break
    if line[0:4]=="node":
        ips=line.split()
        ips.pop(0)
        ips.pop(0)

        if len(ips)>1:
            print(ips)
            for ip in ips:
                ali[ip]=i
            i+=1
print(ali)
anstra=[]
sql = "select tra from trace "
cursor.execute(sql)
for trace in cursor.fetchall():
    trace_ip = trace[0].split()
    for i in range(len(trace_ip)):
        if trace_ip[i] in ali:
            trace_ip[i]="alias"+str(ali[trace_ip[i]])
    anstra.append(trace_ip)
print(anstra)
for tra in anstra:
    str=""
    for t in tra:
        str+=t
        str+=" "
    sql = "INSERT INTO trace_alias(tra) VALUES ('%s')" % (str)
    # 每读取一行的末尾已经有了一个 `\n`
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception as c:
        # 如果发生错误则回滚
        print(c)
        db.rollback()
