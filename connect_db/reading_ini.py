##reading .ini files
import ConfigParser
Config = ConfigParser.ConfigParser()

Config.read("C:\\Users\\soori\\Desktop\\client_secret\\credentials_db.ini")

user_name=Config.get('Section1','name')
host=Config.get('Section1','host')
pwd=Config.get('Section1','password')
