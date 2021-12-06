# import requests

# res = requests.get('http://pfyhy.demo.xiaoi.com/manager1')
# if res.status_code == 200:
#     print("接口访问成功")
# else:
#     print("接口访问失败")


import MySQLdb

conn = MySQLdb.connect(
    host = '',
    port = '',
    user = '',
    passwd = '',
    db = '',
    charset = ''
)

c = conn.cursor()
c.execute('select * from table')

rows = c.fetchall()
print(rows)

for i in range(c.rowcount):

    row = c.fetchone()
    print(row)


