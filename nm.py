import pymysql
db = pymysql.connect("localhost", "root", "root", "bishe")
cursor = db.cursor()
sql = "select tra from trace_alias "
cursor.execute(sql)
nm_dict={}
cnt=0
anstra=[]
#[上一跳,下一跳,跳数]
for trace in cursor.fetchall():
    trace_ip = trace[0].split()
    for i in range(len(trace_ip)):
        if trace_ip[i][0]=='*':
            cnt+=1
            pairs=(trace_ip[i-1],trace_ip[i+1])
            if pairs not in nm_dict:
                nm_dict[pairs]=trace_ip[i]
            else:
                trace_ip[i]=nm_dict[pairs]
    anstra.append(trace_ip)
print(anstra)
flag=0
xn=""
anstra2=[]
for tra in anstra:

    if tra[0][0] == "*":
        if flag == 0:
            xn = tra[0]
            flag = 1
        else:
            tra[0] = xn
    anstra2.append(tra)
anstra3=[]
for tra in anstra2:
    for i in range(len(tra)):
        if tra[i][0]=='*':
            if tra[i+1][0]=='*':
                pairs=(tra[i-1],'*')
                if pairs not in nm_dict:
                    nm_dict[pairs]=tra[i]
                else:
                    tra[i]=nm_dict[pairs]
    anstra3.append(tra)

for tra in anstra3:
    str=""
    for t in tra:
        str+=t
        str+=" "
    sql = "INSERT INTO final_trace(tra) VALUES ('%s')" % (str)
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

