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
            bran={}
            bran["name"]="al"+str(i)

            bran["children"]=[]
            for ip in ips:
                ali[ip]=i
                bran["children"].append({"name":ip})
                sql="INSERT INTO alias (ip,groups) VALUES ('%s','%s')" % (ip,i)
                try:
                    # 执行sql语句
                    cursor.execute(sql)
                    # 提交到数据库执行
                    db.commit()
                except Exception as c:
                    # 如果发生错误则回滚
                    print(c)
                    db.rollback()
            if i<10:
                rootschild.append(bran)
            print(i)
            i+=1
            print(ips)
tree_dict = {
    "name":"alias_tree",
    "children":rootschild,
}

print(tree_dict)
json_str = json.dumps(tree_dict, indent=4)
with open('/home/fy/trace_show/ip_trace/static/tree.json', 'w') as json_file:
    json_file.write(json_str)
sql = "select tra from trace limit 100"
cursor.execute(sql)
ip_all = []
nm=0
nodes=[]
ex_ip={}
al_id={}
now=0
links=[]
for trace in cursor.fetchall():
    trace_ip = trace[0].split()
    i = 0
    pre=0

    for ip in trace_ip:
        ans = now
        if ip[0]=="*":
            jip={}
            jip['name']=ip
            jip['value']=1
            jip['category']=0
            nm=nm+1
            nodes.append(jip)
            now = now + 1
        elif ip in ali:
            jip={}
            if ali[ip] not in al_id:
                al_id[ali[ip]]=now
                jip['name']="al"+str(ali[ip])
                jip['value'] = 1
                jip['category'] = 2
                nodes.append(jip)
                now = now + 1
            else:
                ans=al_id[ali[ip]]
        else:
            jip={}
            if ip not in ex_ip:
                ex_ip[ip]=now
                jip['name']=ip
                jip['value']=1
                jip['category']=1
                nodes.append(jip)
                now = now + 1
                with open("iplist", 'a') as f:  # 'a'表示append,即在原来文件内容后继续写数据（不清楚原有数据）
                    f.write(ip+"\n")
                '''
                sql = "INSERT INTO total_ip(ip) VALUES ('%s')" % (ip)
                try:
                    # 执行sql语句
                    cursor.execute(sql)
                    # 提交到数据库执行
                    db.commit()
                except Exception as c:
                    # 如果发生错误则回滚
                    print(c)
                    db.rollback()
                '''
            else:
                ans=ex_ip[ip]

        if i!=0:
            tlin={}
            tlin["source"]=pre
            tlin["target"]=ans
            links.append(tlin)
        pre=ans

        i=i+1


test_dict = {
    "type": "force",
    "categories":[{
        "name": "匿名",
        "keyword": {},
        "base": "HTMLElement"
    },
        {
            "name": "非匿名",
            "keyword": {},
            "base": "WebGLRenderingContext"
        },{
            "name": "别名集",
            "keyword": {},
            "base": "alias"
        }],
    "nodes": nodes,
    'links':links
}
print(len(nodes))
json_str = json.dumps(test_dict, indent=4)
with open('/home/fy/trace_show/ip_trace/static/alias.json', 'w') as json_file:
    json_file.write(json_str)

