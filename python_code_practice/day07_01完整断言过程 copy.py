# 固定的代码
# 官网给的
import pymysql

DBCONFIG = {
    "host":"43.138.178.63",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"haimo"
}

sql = "select * from tb_system_user where id=1"

# 1. 连接并且操作数据库
database = pymysql.connect(host=DBCONFIG["host"], 
                           port=DBCONFIG["port"], 
                           user=DBCONFIG["user"],
                           password=DBCONFIG["password"], 
                           db=DBCONFIG["database"])
# 2. 获取游标：新建查询窗口
cur = database.cursor()
# 3. 执行sql查询语句
cur.execute(sql)
# 4. 获取结果
res = cur.fetchall()
# 5. 关闭数据连接
database.close()

print(res)



