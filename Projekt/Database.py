from Table import Table
import re,json,shutil
from SQLException import SQLException
class Database:
  def __init__(self,path):
    self.dbpath = path
    if path==":memory:":
      self.data = {"tables":{}}
    else:
      try:
        data = json.load(open(path,"r",encoding='utf-8'))
        self.data = data
        for k in data["tables"]:
          setattr(self,k,Table(data["tables"][k]))
      except IOError:
        self.data = {"tables":{}}
        

  def getTable(self,name):
    if hasattr(self,name):
      return getattr(self,name)
    else:
      raise SQLException("Table doesn't exists")

  def createTable(self,name,columns):
    if hasattr(self,name):
      raise SQLException("Table already exists")
    else:
      self.data["tables"][name]={"columns":columns,"rows":[]}
      setattr(self,name,Table(self.data["tables"][name]))

  def dropTable(self,name):
    table = self.getTable(name)
    self.data["tables"].pop(name)
    delattr(self,name)

  def insertInto(self,table,row,values=[]):
    table = self.getTable(table)
    return table.insert(row,values)

  def selectFrom(self,table,columns=[],where=''):
    table = self.getTable(table)
    return table.select(columns,where)

  def deleteFrom(self,table,where=''):
    if hasattr(self,table):
      return getattr(self,table).delete(where)
    else:
      raise SQLException("Table doesn't exists")

  def updateTable(self,table,data,where):
    if hasattr(self,table):
      return getattr(self,table).update(data,where)
    else:
      raise SQLException("Table doesn't exists")

  def commit(self):
    if self.dbpath==":memory:":
      raise SQLException("Can't commit :memory: database. Use SAVE before")
    shutil.copy(self.dbpath,f'{self.dbpath}.bak')
    json.dump(self.data,open(self.dbpath,'w'))

  def rollback(self):
    if self.dbpath==":memory:":
      raise SQLException("Can't rollback :memory: database.")
    self.__init__(self.dbpath)

  def saveto(self,path):
      json.dump(self.data,open(path,'w'))
      self.dbpath = path

if __name__=="__main__":
  db = Database('testdb.json')
  print(db.selectFrom('tabela1'))
  db.updateTable('tabela1',{"id":99},where="id==3")
  print(db.selectFrom('tabela1'))