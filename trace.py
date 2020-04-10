from scapy.all import *
import gzip
import pymysql
import geoip2.database
reader = geoip2.database.Reader("/home/fy/city/GeoLite2-City.mmdb")

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "bishe")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
cnt=0
result_1=""
while cnt<50:
    cnt=cnt+1
    sql="select ip from ip_loc where flag=0 limit 1"
    fl=0
    try:
        # 执行sql语句
        cursor.execute(sql)

        # 提交到数据库执行
        db.commit()
        result_1 = cursor.fetchone()[0]
        print(result_1)
        ans, unans = traceroute(result_1, timeout=5)
        s = "111.41.172.178 "
        i = 1
        ip_list = []
        for snd, rcv in ans:
            ip_list.append((snd.ttl, rcv.src))
        ip_list.sort(key=lambda x: x[0])
        for a in ip_list:

            try:
                response = reader.city(a[1])
                sql = "INSERT INTO ip_loc(ip,lat, lon,flag) VALUES ('%s','%s','%s','%d')" % (
                    a[1], response.location.latitude, response.location.longitude, 0)
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
            except Exception as e:
                print(e)
            #print(a[1])
            while i < a[0]:
                # print(i,snd.ttl)
                s += '*'
                s += ' '
                i = i + 1
            if i != 1:
                s += a[1]
                s += ' '

                if result_1 == a[1]:
                    fl=1
                    break
            i = i + 1
        print(s)
        if fl!=0:
            
            sql="INSERT INTO trace(dip,tra) VALUES ('%s','%s')"% (result_1,s)
            try:
                # 执行sql语句
                cursor.execute(sql)

                # 提交到数据库执行
                db.commit()
            except Exception as c:
                # 如果发生错误则回滚
                print(c)
                db.rollback()
        sql = "update ip_loc set flag=1 where ip='"+result_1+"'"
        try:
            # 执行sql语句
            cursor.execute(sql)

            # 提交到数据库执行
            db.commit()
        except Exception as c:
            # 如果发生错误则回滚
            print(c)
            db.rollback()
    except Exception as c:
        # 如果发生错误则回滚
        print(c)
        db.rollback()



