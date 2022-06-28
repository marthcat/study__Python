import enum
from debugpy import connect
import pymysql
from requests import delete

class Pymysql_test() :
  #변수 설정 global 
  conn= None 
  cur = None
  host, port = None, None
  user, password = None, None
  db = None
  charset = None

  def __init__(self, host='127.0.0.1', port=3306, user="", password="", db = "", charset="utf8") :
    self.SetConnectionInfo(host, port, user, password, db, charset) 
    
  def SetConnectionInfo(self, host=None, port=None, user=None, password=None, db=None, charset=None) :
    if     host != None : self.host     = host
    if     port != None : self.port     = port
    if     user != None : self.user     = user
    if password != None : self.password = password
    if       db != None : self.db       = db
    if  charset != None : self.charset  = charset 

  def Connect(self):
    self.conn = pymysql.connect(
                      host = self.host, 
                      port = self.port,
                      user = self.user,
                      password = self.password,
                      db= self.db,
                      charset= self.charset)

  def Disconnect(self):
    self.conn.close()

  def Execute(self, query):
    self.cur = self.conn.cursor()   
    
    return self.cur.execute(query)

  def FetchAll(self):
    return self.cur.fetchall()

  def FetchOne(self):
    return self.cur.fetchone()

  def Rollback(self):
    self.conn.rollback()

  def Commit(self):
    self.conn.commit()


##--------------------------------------------------------------------------
## pip
## pip install cryptography

class testWorkEnum(enum):
  CreateDB = 1
  CreateTable = 2
  InsertData = 3
  Select = 4
  DeleteTable = 5
  DeleteDB = 6

test = [testWorkEnum.CreateDB, testWorkEnum.CreateTable, testWorkEnum.InsertData, testWorkEnum.Select, testWorkEnum.DeleteTable, testWorkEnum.DeleteDB]

if __name__ == "__main__":
  sql = Pymysql_test(user='root', password='1234', host='127.0.0.1')
  if testWorkEnum.CreateDB in test :
    sql.Connect()    
    sql.Execute("CREATE DATABASE IF NOT EXISTS testpymysql")
    sql.commit()
  if testWorkEnum.CreateTable in test :   
    pass
  if testWorkEnum.InsertData in test :   
    pass
  if testWorkEnum.Select in test :
    # sql.SetConnectionInfo(db="employees") 
    # sql.Connect()
    # qlen = sql.Execute("select * from titles")
    # print("-test-1: {}".format(qlen))  
    # for f in sql.FetchAll():
    #   print(f)    
    sql.SetConnectionInfo(db="sakila") 
    sql.Connect()
    qlen = sql.Execute("select * from actor")
    print("-test-2: {}".format(qlen))
    for f in range(qlen):
      print(sql.FetchOne())
  if testWorkEnum.DeleteTable in test :
    pass
  if testWorkEnum.DeleteDB in test :
    pass
  

