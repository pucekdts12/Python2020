import re
from SQLException import SQLException

class Table:
  def __init__(self,data):
    self.rows = data["rows"]
    self.columns = data["columns"]
    self.columns_ind = { col:i for i,col in enumerate(self.columns) }

  def old_where(self,row,where):
    for fn in where:
      if fn(row)==False: return False
    return True

  def where(self,row,where=''):
    if where=='': return True
    try:
      #change alone '='  in SQL comparision to '==' for eval
      where = re.sub(r'([^<>!=])=([^<>!=])',r'\1==\2',where)


      # [^\s\"\']+ - cokolwiek bez spacji,',"
      # | lub
      # \"[^\"]*\" - wyraz ze spacja w ""
      # | lub
      # \'[^\']*\' - wyraz ze spacja w ''
      tmp = re.findall(r'[^\s\"\']+|\"[^\"]*\"|\'[^\']*\'',where) 
      eval_str = ''
      prev = ''
      i = 0
      while i < len(tmp):
        w = tmp[i]
        if w[0]==')' or w[0]=='(':
          eval_str+=w[0]
          w = w[1:]

        if w.upper()=='LIKE':
          # eval_str+=f'bool(re.search({tmp[i+1]},{prev}))'
          eval_str+=f'bool(re.search({tmp[i+1]},{prev},flags=re.IGNORECASE))'
          prev = ''
          i+=1
        elif w.upper()=='OR':
          eval_str+=f'{prev} or '
          prev = ''
        elif w.upper()=='AND':
          eval_str+=f'{prev} and '
          prev = ''
        
        else:
          eval_str+=prev
          prev = w
        i+=1
      eval_str+=prev
    except:
      raise SQLException("Invalid Syntax near WHERE")
    try:
      return eval(eval_str,{"re":re},row)
    except BaseException as e:
      raise SQLException(str(e))
    
    

  def select(self,columns = [],where = ''):
    ret = []
    for row in self.rows:
      row = dict(zip(self.columns,row))
      append = False
      if self.where(row,where):
        append = True
      if columns!=[]: # columns to show
        row = { col:row[col] for col in columns if col in row}
      if append:
        ret.append(row)

    return ret

  def insert(self,row,values=[]):
    if type(row) is list:
      if values!=[]:
        values = { col:i for i,col in enumerate(values) }
        new_row = []
        for col in self.columns:
          if col in values:
            new_row.append( row[ values[col] ] )
          else:
            new_row.append(None)
        self.rows.append(new_row)
      else:
        self.rows.append(row)
    elif type(row) is dict:
      new_row = []
      for col in self.columns:
        if col in row:
          new_row.append(row[col])
        else:
          new_row.append(None)
      self.rows.append(new_row)
    return 1

  def update(self,data,where):
    self.columns_ind
    num = 0
    for list_row in self.rows:
      row = dict(zip(self.columns,list_row))
      append = False
      if self.where(row,where):
        for col in data:
          list_row[ self.columns_ind[col] ] = data[col]
        num+=1
    return num
      

  def delete(self,where = []):
    num,i = 0,0
    while i<len(self.rows):
      row = dict(zip(self.columns,self.rows[i]))
      if self.where(row,where):
        self.rows.pop(i)
        num+=1
      else:
        i+=1
    return num
