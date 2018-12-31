import pymysql

class MySql_Connect:
    def insert(self, list, tableName):
        #config = {
        #    'host':'127.0.0.1',
        #    'port':'3306',
        #    'user':'root',
        #    'password':'520520',
        #    'charset':'utf8mb4',
        #    'cursorclass':pymysql.cursors.DictCursor
        #    }
        #conn = pymysql.connect(**config)
        conn = pymysql.connect('127.0.0.1','root','520520','spiderD')
        a = conn.cursor()
        data = ""

        for i in range(len(list)):
            list[i] = '"' + list[i] + '"'
           

        data = ','.join(list)
        sql_str = "insert ignore into {} values(ID,{});".format(tableName, data)
        print("sql语句：" + sql_str)
        a.execute(sql_str)

        #真正的执行
        conn.commit()
        a.close()
    