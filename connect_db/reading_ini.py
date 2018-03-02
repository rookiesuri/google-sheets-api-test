##reading .ini files
import ConfigParser
Config = ConfigParser.ConfigParser()

Config.read("C:\\Users\\soori\\Desktop\\client_secret\\New folder\\query_test.ini")
z=Config.sections()
print z


##### reading a json
