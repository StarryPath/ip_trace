import pymysql
db = pymysql.connect("localhost", "root", "root", "bishe")
cursor = db.cursor()
sql = "select tra2 from nm2 "
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
for tra in anstra:
    str=""
    for t in tra:
        str+=t
        str+=" "
    sql = "INSERT INTO nm3(tra3) VALUES ('%s')" % (str)
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
