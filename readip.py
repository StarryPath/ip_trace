import pymysql
import geoip2.database
reader = geoip2.database.Reader("/home/fy/city/GeoLite2-City.mmdb")

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "bishe")

# 使用cursor()方法获取操作游标 
cursor = db.cursor()



file = open("result2.txt")

while True:
    ip = file.readline()  # 只读取一行内容
    ip = ip.strip('\n')
    if not ip:
        break
    try:
        response = reader.city(ip)
    # 判断是否读取到内容
        sql = "INSERT INTO ip_loc(ip,lat, lon) VALUES ('%s','%s','%s')" % (ip, response.location.latitude, response.location.longitude)
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
file.close()
# 关闭数据库连接
db.close()