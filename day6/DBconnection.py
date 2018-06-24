#下载并导入代码库：pymysql

import pymysql


class DBConnection:
    def execute_sql_command(self):

        #2.获取数据库连接
        conn = pymysql.Connect(host='127.0.0.1', user='root', password="root",
                 database='pirate', port=3306,
                 charset='utf8')
        try:
        #3.获取数据库游标
            cursor = conn.cursor()
            sql ='select * from hd_user order by id desc'

        #5.通过游标执行语句
            cursor.execute(sql)
        #6.
       # all_result = cursor.fetchall()
            row = cursor.fetchone()
            print(row)
            conn.commit()
        finally:
            conn.close()
if __name__ == '__main__':
    DBConnection().execute_sql_command()