import MySQLdb as mysql


import time
import json

db = mysql.connect(host='localhost', user='root',
                   password='root', db="INFORMATION_SCHEMA")
cur = db.cursor()

cur.execute('SHOW STATUS')
res = cur.fetchall()

r = dict(res)
cur.execute("select ID,DB from PROCESSLIST")
res1 = cur.fetchall()


print(f"Uptime => {r['Uptime']}")
print(f"Threads_created => {r['Threads_created']}")
print(f"Threads_connected => {r['Threads_connected']}")
print(f"Threads_running => {r['Threads_running']}")
print(f"Queries => {r['Queries']}")
print(f"Max_used_connections => {r['Max_used_connections']}")

print("process list :",res1)
cur.close()
