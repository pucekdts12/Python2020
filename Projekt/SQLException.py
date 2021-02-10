class SQLException(BaseException):
  def __init__(self,msg):
    self.message = msg