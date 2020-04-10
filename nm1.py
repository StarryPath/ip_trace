import subprocess
import sys
import re
import matplotlib.pyplot as plt
import  pywt
import numpy as np
import pymysql
# 常用编码
GBK = 'gbk'
UTF8 = 'utf-8'

# 解码方式，一般 py 文件执行为utf-8 ，cmd 命令为 gbk
current_encoding = GBK
db = pymysql.connect("localhost", "root", "root", "bishe")
cursor = db.cursor()
sql="select dip from trace where re is null"
cursor.execute(sql)
for dip in cursor.fetchall():
    print(dip[0])
    popen = subprocess.Popen(['ping', '-i 0.1',"-c 20",dip[0]],
                             stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE,
                             bufsize=1)
    list1 = []
    # 重定向标准输出202.115.0.0
    while popen.poll() is None:         # None表示正在执行中
        r = popen.stdout.readline().decode(current_encoding)
        #print(r)
        s = r.find("time=")
        if  s > 0:
            list_s = list(r[s+5:-3])
            r = "".join(list_s)
            #print(float(r))
            if r :
                list1.append(float(r))

    print(list1)
    # 重定向错误输出
    if popen.poll() != 0:                      # 不为0表示执行错误
        err = popen.stderr.read().decode(current_encoding)
        sys.stdout.write(err)                 # 可修改输出方式，比如控制台、文件等
    list2 = []
    list3 = []
    j = 0

    for i in range(0,len(list1)):
        list2.append(int(i))
    print(list2)

    try:
        wp = pywt.WaveletPacket(data = list1, wavelet='db1', maxlevel = 3 )
        aaa = wp['aaa'].data
        aad = wp['aad'].data
        ada = wp['ada'].data
        add = wp['add'].data
        daa = wp['daa'].data
        dad = wp['dad'].data
        dda = wp['dda'].data
        ddd = wp['ddd'].data
        re1 = np.linalg.norm(aaa, ord = None)
        re2 = np.linalg.norm(aad, ord = None)
        re3 = np.linalg.norm(ada, ord = None)
        re4 = np.linalg.norm(add, ord = None)
        re5 = np.linalg.norm(daa, ord = None)
        re6 = np.linalg.norm(dad, ord = None)
        re7 = np.linalg.norm(dda, ord = None)
        re8 = np.linalg.norm(ddd, ord = None)
        re = [re2, re3, re4, re5, re6, re7, re8]
        re_str=""
        for i in re:
            re_str=re_str+str(i)+" "

        sql = "update trace set re='"+re_str+"'where dip='" + dip[0] + "'"
        try:
            # 执行sql语句
            cursor.execute(sql)

            # 提交到数据库执行
            db.commit()
        except Exception as c:
            # 如果发生错误则回滚
            print(c)
            db.rollback()
        print(re)
    except Exception as e:
        print(e)