import pymysql

DBCONFIG = {
    "host":"43.138.178.63",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"haimo"
}

class MysqlTools():
    def __init__(self, host=DBCONFIG["host"], 
                 port=DBCONFIG["port"],
                 user=DBCONFIG["user"],
                 password=DBCONFIG["password"],
                 database=DBCONFIG["database"]):
        self.database = database
        self.host = host
        self.user = user
        self.port = port
        self.password = password
        self.connect = self.get_database_connect()

    # 创建连接并且连接对象
    def get_database_connect(self):
        return pymysql.connect(host=self.host, 
                               port=self.port, 
                               user=self.user,
                               password=self.password,
                               database=self.database)
    
    # 获取游标
    def get_database_cursor(self):
        return self.connect.cursor()

    # 执行sql语句
    def query(self, sql):
        cur = self.get_database_cursor()
        cur.execute(sql)
        return cur.fetchall()

    # 析构方法：关闭数据连接，释放资源
    def __del__(self):
        self.connect.close()

if __name__ == '__main__':
    sql = "select * from tb_system_user where id=1"
    result = MysqlTools().query(sql)
    print(result)
