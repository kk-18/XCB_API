import pymysql

class SQLclient:
    def sql_client(self,sql):
       #打开数据库连接
        conn=pymysql.connect(host='114.116.136.190',user='root',password='a175a9c176',port=13306)
        #使用cursor()方法创建一个游标对象cursor
        cursor=conn.cursor() #游标对象用于执行查询和获取结果
        #使用execute()方法执行sql
        cursor.execute(sql)
        # 数据库里增、删、改的时候，必须要进行提交，否则插入的数据不生效
        conn.commit()
        #使用fetchone()方法获取单条数据
        data=cursor.fetchone()
        #关闭数据库连接
        conn.close()
        return data