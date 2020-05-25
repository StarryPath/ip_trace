import pymysql
db = pymysql.connect("localhost", "root", "root", "bishe")
cursor = db.cursor()
sql = "select tra1 from nm1 "
cursor.execute(sql)
nm_dict={}
cnt=0
anstra=[]
flag=0
xn=""
#[上一跳,下一跳,跳数]
for trace in cursor.fetchall():
    trace_ip = trace[0].split()
    if trace_ip[0][0]=="*":
       if flag==0:
            xn=trace_ip[0]
            flag=1
       else:
            trace_ip[0]=xn
    anstra.append(trace_ip)
print(anstra)

for tra in anstra:
    str=""
    for t in tra:
        str+=t
        str+=" "
    sql = "INSERT INTO nm2(tra2) VALUES ('%s')" % (str)
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
#anslist=sorted(nm_dict.items(),key=lambda item:len(item[1]),reverse = True)
#for i in anslist:
  #  print(i)
print(nm_dict)
print(cnt)

