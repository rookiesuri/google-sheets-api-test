##connect_db
##django-admin startproject connectpg starts project dont use .py

import psycopg2

try:
    conn = psycopg2.connect("dbname='spoyldev' user='' host='' password=''")
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



