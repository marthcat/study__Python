from enum import Enum
import pymysql

class Pymysql_worker() :
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

  def Close(self):
    self.cur.close()
    self.conn.close()

  def Execute(self, query):
    self.cur = self.conn.cursor()          
    return self.cur.execute(query)

  def ExecuteDict(self, query):
    self.cur = self.conn.cursor(pymysql.cursors.DictCursor)          
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

class TestWorkEnum(Enum) :
  CreateDB = 1
  CreateTable = 2
  InsertData = 3
  Select = 4
  DeleteTable = 5
  DeleteDB = 6

test = [TestWorkEnum.CreateDB, TestWorkEnum.CreateTable, TestWorkEnum.InsertData, TestWorkEnum.Select, TestWorkEnum.DeleteTable, TestWorkEnum.DeleteDB]
# test = [TestWorkEnum.Select]

if __name__ == "__main__":
  sql = Pymysql_worker(user='root', password='1234', host='127.0.0.1')

  if TestWorkEnum.CreateDB in test :
    sql.Connect()    
    sql.Execute("CREATE DATABASE IF NOT EXISTS testpymysql")
    sql.Commit()
    print("--CreateDB--")

  if TestWorkEnum.CreateTable in test :   
    sql.SetConnectionInfo(db="testpymysql", charset='utf8')
    sql.Connect()    
    query = '''CREATE TABLE IF NOT EXISTS tblGood (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(20) NOT NULL,                          
                text VARCHAR(20) NULL
               )
            '''
    sql.Execute(query)
    sql.Commit()
    print("--CreateTable--")
    
  if TestWorkEnum.InsertData in test :   
    sql.SetConnectionInfo(db="testpymysql") 
    sql.Connect()
    sql.Execute("INSERT INTO tblGood(name, text) VALUE('AAA','111')")
    sql.Execute("INSERT INTO tblGood(name, text) VALUE('BBB','222')")
    sql.Execute("INSERT INTO tblGood(name, text) VALUE('CCC','333')")
    sql.Commit()
    print("--InsertData--")

  if TestWorkEnum.Select in test :
    # sql.SetConnectionInfo(db="employees") 
    # sql.Connect()
    # qlen = sql.Execute("select * from titles")
    # print("-test-1: {}".format(qlen))  
    # for f in sql.FetchAll():
    #   print(f)    
    # sql.SetConnectionInfo(db="sakila") 
    # sql.Connect()
    # qlen = sql.Execute("select * from actor")
    # print("-test-2: {}".format(qlen))
    # for f in range(qlen):
    #   print(sql.FetchOne())
    sql.SetConnectionInfo(db="testpymysql") 
    sql.Connect()
    qlen = sql.Execute("select * from tblGood")
    print(type(sql))
    for f in range(qlen):
      print(sql.FetchOne())
    print("--Select--")

  if TestWorkEnum.DeleteTable in test :
    sql.SetConnectionInfo(db="testpymysql") 
    sql.Connect()    
    sql.Execute("DROP Table IF EXISTS tblGood")
    sql.Commit()
    print("--DeleteTable--")

  if TestWorkEnum.DeleteDB in test :
    sql.Connect()    
    sql.Execute("DROP DATABASE testpymysql")
    sql.Commit()
    print("--DeleteDB--")

  sql.Close()
  

