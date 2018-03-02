##connect_db
##django-admin startproject connectpg starts project dont use .py

import psycopg2

##get credentials
import ConfigParser
Config = ConfigParser.ConfigParser()

Config.read("C:\\Users\\soori\\Desktop\\client_secret\\credentials_db.ini")

user_name=" user='"+Config.get('Section1','name')+"'"
host_ini=" host='"+Config.get('Section1','host')+"'"
pwd_ini=" password='"+Config.get('Section1','password')+"'"
dbname_ini=" dbname='"+Config.get('Section1','dbname')+"'"
conn_string=user_name+host_ini+pwd_ini+dbname_ini
print conn_string


##########
try:
    conn = psycopg2.connect(conn_string)
except:
    print "I am unable to connect to the database"

cur=conn.cursor()
cur.execute("""select id,date_created from catalogue_product limit 10""")

rows=cur.fetchall()
# print rows
print rows[0]
print rows[0][0]
print type(rows[0])
print len(rows[0])
