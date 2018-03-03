import psycopg2
import ConfigParser

Config = ConfigParser.ConfigParser()

Config.read("C:\\Users\\soori\\Desktop\\client_secret\\credentials_db.ini")
# conn_string=Config.get('Section2','conn_string')
# conn = psycopg2.connect(conn_string)
# cur=conn.cursor()
def test_con():

    conn_string=Config.get('Section2','conn_string')
    conn = psycopg2.connect(conn_string)
    cur=conn.cursor()
    return cur

z=test_con()
z.execute("""select current_date""")

print z.fetchall()
