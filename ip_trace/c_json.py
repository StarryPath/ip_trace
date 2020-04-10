from collections import defaultdict, OrderedDict
import json
import pymysql
db = pymysql.connect("localhost", "root", "root", "bishe")
cursor = db.cursor()
sql = "select tra from trace limit 100"
cursor.execute(sql)
ip_all = []
nm=0
nodes=[]
ex_ip={}

now=0
links=[]
for trace in cursor.fetchall():
    trace_ip = trace[0].split()
    i = 0
    pre=0

    for ip in trace_ip:
        ans = now
        if ip=="*":
            jip={}
            jip['name']="*"+str(nm)
            jip['value']=1
            jip['category']=0
            nm=nm+1
            nodes.append(jip)
            now = now + 1

        else:
            jip={}
            if ip not in ex_ip:
                ex_ip[ip]=now
                jip['name']=ip
                jip['value']=2
                jip['category']=1
                nodes.append(jip)
                now = now + 1
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
        }],
    "nodes": nodes,
    'links':links
}

json_str = json.dumps(test_dict, indent=4)
with open('/home/fy/trace_show/ip_trace/static/webkit-dep.json', 'w') as json_file:
    json_file.write(json_str)
