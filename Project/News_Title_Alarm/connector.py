import pymysql

config = {'user' : 'root',
          'password' : '1w6z7z6z',
          'host' : '127.0.0.1',
          'database' : 'python',
          'port' : 3307}
    
def getConn():
    con = pymysql.connect(**config)
    return con