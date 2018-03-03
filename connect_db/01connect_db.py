##connect_db
##django-admin startproject connectpg starts project dont use .py

import psycopg2

##get credentials
import ConfigParser
Config = ConfigParser.ConfigParser()

Config.read("C:\\Users\\soori\\Desktop\\client_secret\\credentials_db.ini")


conn_string=Config.get('Section2','conn_string')
print conn_string


##########
try:
    conn = psycopg2.connect(conn_string)
except:
    print "I am unable to connect to the database"

cur=conn.cursor()
cur.execute("""select current_date""")

rows=cur.fetchall()
# print rows
print rows[0]
print rows[0][0]
print type(rows[0])
print len(rows[0])
