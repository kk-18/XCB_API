import pymysql

class SQLclient:
    def sql_client(self,sql):
       #打开数据库连接
        conn=pymysql.connect(host='114.116.136.190',user='root',password='a175a9c176',port=13306)
        #使用cursor()方法创建一个游标对象cursor
        cursor=conn.cursor() #游标对象用于执行查询和获取结果
        #使用execute()方法执行sql
        cursor.execute(sql)
        #使用fetchone()方法获取单条数据
        data=cursor.fetchone()
        #关闭数据库连接
        conn.close()
        return data
sql="""
 select id from db_xcb.t_order where uid=22
"""
sss=SQLclient().sql_client(sql)
print(sss)