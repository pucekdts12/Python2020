import copy,json,sys,re,shutil,cmd,argparse
from Database import Database
from SQLException import SQLException

class dbCmd:
  def __init__(self,db):
    self.db = db
    print("Current Database:",db.dbpath)
    special = { '.exit':self.exit,'.schema':self.schema,'.file':self.fileinfo,'.save':self.save,'.open':self.opendb}
    for k in special:
      setattr(self,f'do_{k}',special[k])

  def cmdloop(self):
    exit = False
    while exit!=True:
      line = input("db> ")
      match = re.search("([^ ]+)",line)
      if match:
        command = match.group(1)
        line = line[match.end()+1:]
        # print([command,line])
        if hasattr(self,f'do_{command}'):
          exit = getattr(self,f'do_{command}')(line)
        else:
          print("Unrecognized Command")
      else:
        print("Unrecognized Command")

  def exit(self,arg):
    return True

  def do_help(self,arg):
    msg_main="""Program help:
  help - this message
  .exit - exits shell
  .open <file_path> - open database in file if file doesn't exists it'll creates file on save
  .save <file_path> - saves database to file and switches to it
  .file - shows current database file
  .schema - shows current database tables

SQL Help(case-sensitive):
  SELECT * | col[,cols...] FROM table [WHERE ...]
  INSERT INTO table[(cols...)] VALUES(vals...)
  DELETE FROM table [WHERE ...]
  UPDATE table SET col1=val1[,...] [WHERE ...]
  CREATE TABLE table(col1,[cols...])
  DROP TABLE table
  COMMIT
  ROLLBACK

WHERE conditions examples:
  id=1 AND name LIKE '<regex>'
  id=2 OR (name LIKE '<regex>' AND year<2000)"""
    print(msg_main)

  def save(self,arg):
    if arg=='':
      print("usage: SAVE file_path")
    else:
      try:
        self.db.saveto(arg)
      except Exception as e:
        print("Exception:",e)

  def opendb(self,arg):
    try:
      self.db = Database(arg)
      print(f'Database {arg} loaded.')
    except:
      print('Failed to load database',arg)

  def schema(self,arg):
    # print(self.db.data)
    print(f"Tables in database[{self.db.dbpath}]:")
    for t in self.db.data["tables"]:
      tab = self.db.data["tables"][t]
      print(f'{t}({",".join(tab["columns"])})')

  def fileinfo(self,arg):
    print("Database",self.db.dbpath)

  def do_SELECT(self,arg):
    where = re.findall(r'WHERE (.*)$',arg)
    where = where[0] if where else ''
    cols = re.findall(r'^(.+?) FROM',arg)
    try:
      try:
        cols = cols[0]
        table = re.findall(r'FROM (.+?)($| WHERE)',arg)
        table = table[0][0]
      except:
        raise SQLException("Invalid Syntax near SELECT")

      tableCols = self.db.getTable(table).columns
      columns = tableCols
      if cols!='*':
        columns = cols.split(',')    
        
      for col in columns:
        if col not in tableCols:
          raise SQLException(f'column {col} doesn\'t exists')

      rows = self.db.selectFrom(table,columns,where)
      print('|'.join(columns))
      for row in rows:
        line=[]
        for col in columns:
          line.append(str(row[col]))
        print('|'.join(line))
    except SQLException as e:
      print("SQLException: ",e.message)

  def do_INSERT(self,arg):
    try:
      table = re.search(r'INTO (.+?) VALUES',arg).group(1)
      match = re.search(r'\(.+?\)',table)
      columns = []
      if match:
        columns = match.group(0)[1:-1].split(',')
        table = table[:match.start()]
    except:
      print("SQLException: ","Invalid Syntax near INTO")
      return False
    try:
      values = re.search(r'VALUES {0,1}\((.+)\)$',arg).group(1).split(',')
      data = []
      for val in values:
        val = dbCmd.valConvert(val)
        data.append(val)


    except Exception as e:
      print("Invalid Syntax near VALUES: ",e)
      return False
    try:
      num = self.db.insertInto(table,data,columns)
      print('Rows affected:',num)
    except SQLException as e:
      print("SQLException: ",e.message)
    
  def do_UPDATE(self,arg):
    where = re.search(r'WHERE (.*)$',arg)
    if where:
      arg = arg[:where.start()]
      where = where.group(1)
    else:
      where = ''

    try:
      table = re.search(r'(.+?) SET',arg).group(1)
      data = re.search(r'SET (.+?)$',arg).group(1)
      values = {}
      for set in data.split(','):
        tmp = set.split('=',1)
        val = re.search(r'[^\s\'\"]+|\'[^\']+\'|\"[^\"]+\"',tmp[1]).group(0)
        val = dbCmd.valConvert(val)
        values[tmp[0]] = val
        
      num = self.db.updateTable(table,values,where)
      print('Rows affected:',num)
    except SQLException as e:
      print("SQLException:",e.message)
    except Exception as e:
      print(e)

  def do_DELETE(self,arg):
    where = re.findall('WHERE (.*)$',arg)
    if where:
      where = where[0]
    else:
      where = ''
    try:
      table = re.findall('FROM (.+?)($| WHERE)',arg)
      table = table[0][0]
    except:
      raise SQLException("Invalid Syntax near SELECT")
    try:
      num = self.db.deleteFrom(table,where)
      print('Rows affected:',num)
    except SQLException as e:
      print("SQLException:",e.message)
    except Exception as e:
      print("Exception:",e)

  def do_CREATE(self,arg):
    try:
      table = re.search(r'TABLE (.+?)$',arg).group(1)
      match = re.search(r'\(.+?\)',table)
      columns = match.group(0)[1:-1].split(',')
      table = table[:match.start()]
    except:
      print("SQLException: ","Invalid Syntax near TABLE")
      return False
    try:
      self.db.createTable(table,columns)
    except SQLException as e:
      print("SQLException: ",e.message)

  def do_DROP(self,arg):
    try:
      table = re.search('^TABLE (.+?)$',arg).group(1)
    except:
      print('Invalid Syntax near ^')
      return False
    try:
      self.db.dropTable(table)
    except SQLException as e:
      print("SQLException: ",e.message)

  def do_COMMIT(self,arg):
    try:
      self.db.commit()
      print("Database saved.")
    except SQLException as e:
      print("SQLException: ",e.message)
    except Exception as e:
      print("Database *not* saved",e)

  def do_ROLLBACK(self,arg):
    try:
      self.db.rollback()
      print("Database restored.")
    except SQLException as e:
      print("SQLException: ",e.message)
    except:
      print("Database *not* restored")

  @staticmethod
  def valConvert(val):
    if re.search(r'^\'[^\']+\'|^\"[^\"]+\"',val):
      val = str(val).strip('\'" ')
      # print('str',val)
    elif re.search(r'^\d+\.\d+',val):
      val = float(val)
      # print('float',val)
    elif re.search(r'^\d+',val):
      val = int(val)
      # print('int',val)
    return val
    
  
if __name__=="__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("file",help="file with database [default=:memory:]",nargs='?',type=str,default=":memory:")
  args = parser.parse_args()
  app = dbCmd(Database(args.file))
  app.cmdloop()
  
