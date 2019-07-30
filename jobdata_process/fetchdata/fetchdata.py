# encoding:utf-8

import pymysql

class fetchdata():
    def __init__(self):
        self.conn=pymysql.connect(host="localhost",user="root",password='12345678',database='job',charset='utf8')
        self.cursor=self.conn.cursor()
    def fetchdata(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def close(self):
        self.cursor.close()
        self.conn.close()
