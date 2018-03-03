#final file of my funcs
#added query query_reader and connect_db
#to change db credentials change here
import psycopg2
import ConfigParser


###query_reader starts

def query_reader(filename_in):
    inst= open(filename_in,'r')
    out_query = inst.read().replace('\n',' ')
    return out_query

#### connect_db pg connection cursor comes up
# to change db credntials change here

Config = ConfigParser.ConfigParser()
Config.read("C:\\Users\\soori\\Desktop\\client_secret\\credentials_db.ini")

def test_con():
    conn_string=Config.get('Section2','conn_string')
    conn = psycopg2.connect(conn_string)
    cur=conn.cursor()
    return cur
