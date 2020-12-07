import sys,functools,unittest

# dekorator ktory zamienia drugi argument funkcji na Frac
def prepare_frac(fn):
  @functools.wraps(fn)
  def wrapper(*args,**kwargs):
    o = args[1]
    if type(o)==int:
      o = Frac(o,1)
    elif type(o)==float:
      o = Frac(*o.as_integer_ratio())
    elif type(o)==Frac:
      pass
    else:
      raise ValueError("Unsupported type")
    return fn(args[0],o)
  return wrapper


class Frac:
  """Klasa reprezentująca ułamek."""
  def __init__(self, x=0, y=1):
    if y==0:
      raise ValueError("self.y cannot be 0")
    self.x = x
    self.y = y

  def __str__(self):    return f'{self.x}/{self.y}' if self.y!=1 else str(self.x)
  def __repr__(self):   return f'Frac({self.x}, {self.y})'
  def __eq__(self, o):  return self.x==o.x and self.y==o.y
  def __ne__(self, o):  return not self == o
  def __lt__(self, o):  return float(self)<float(o)
  def __le__(self, o):  return float(self)<=float(o)
  def __gt__(self, o):  return float(self)>float(o)
  def __ge__(self, o):  return float(self)>=float(o)

  @prepare_frac
  def __add__(self, o):
    return Frac(self.x*o.y+o.x*self.y,self.y*o.y)

  __radd__ = __add__

  @prepare_frac
  def __sub__(self, o):
    return Frac(self.x*o.y-o.x*self.y,self.y*o.y)

  @prepare_frac
  def __rsub__(self,o):
    return o-self

  @prepare_frac
  def __mul__(self, o):
    return Frac(self.x*o.x,self.y*o.y)

  __rmul__ = __mul__

  @prepare_frac
  def __div__(self, o):
    return Frac(self.x*o.y,self.y*o.x)

  @prepare_frac
  def __rdiv__(self, o):
    print('TYPE',type(o))
    return o/self

  @prepare_frac
  def __truediv__(self, o):
    return Frac(self.x*o.y,self.y*o.x)

  @prepare_frac
  def __rtruediv__(self, o):
    return o/self

  def __floordiv__(self, o):  return float(self)//float(o)
  def __rfloordiv__(self, o): return float(o)//float(self)
  def __mod__(self, o):       return float(self)%float(o)

  # operatory jednoargumentowe
  def __pos__(self):    return self

  def __neg__(self):    return Frac(-self.x, self.y)

  def __invert__(self): return Frac(self.y, self.x)

  def __float__(self):  return self.x/self.y

  def __hash__(self):   return hash(float(self))

class TestFrac(unittest.TestCase):
  def test_str(self):
    f = Frac(1,2)
    self.assertEqual(str(f),'1/2')
    self.assertEqual(f.__repr__(),'Frac(1, 2)')

  def test_float(self):
    f = Frac(1,2)
    self.assertEqual(float(f),0.5)

  def test_exceptions(self):
    fn = lambda x:x # unsupported type
    p1 = Frac(1,1)
    with self.assertRaises(ValueError):
      tmp = Frac(2,0)
      tmp = p1//fn
      tmp = p1/fn
      tmp = p1*fn
      tmp = p1+fn
      tmp = p1-fn
      tmp = p1%fn


  def test_compare(self):
    f1 = Frac(1,2)
    f2 = Frac(1,2)
    f3 = Frac(2,1)
    self.assertTrue(f1==f2)
    self.assertFalse(f1!=f2)
    self.assertFalse(f3==f2)
    self.assertTrue(f3!=f2)
    
    self.assertFalse(f1<f2)
    self.assertTrue(f1<f3)
    self.assertTrue(f1<=f2)

    self.assertFalse(f1>f2)
    self.assertTrue(f3>f1)
    self.assertTrue(f1>=f2)


  def test_operations(self):
    f1 = Frac(1,2)
    f2 = Frac(2,1)
    self.assertEqual( f1+f1  ,Frac(4,4))     # +frac
    self.assertEqual( f2+2   ,Frac(4,1))      # +int
    self.assertEqual( 2+f2   ,Frac(4,1))      # int+
    self.assertEqual( f1+0.5 ,Frac(4,4))    # +float
    self.assertEqual( 0.5+f1 ,Frac(4,4))    # float+

    self.assertEqual( f1-f1  ,Frac(0,4))     # -frac
    self.assertEqual( f2-3   ,Frac(-1,1))     # -int 
    self.assertEqual( 3-f2   ,Frac(1,1))      # int-
    self.assertEqual( f1-1.5 ,Frac(-4,4))   # -float
    self.assertEqual( 1.5-f1 ,Frac(4,4))    # float-

    self.assertEqual( f1*f2  ,Frac(2,2))     # *frac
    self.assertEqual( f2*2   ,Frac(4,1))     # *int
    self.assertEqual( 2*f2   ,Frac(4,1))     # int*
    self.assertEqual( f2*0.5 ,Frac(2,2))     # *float
    self.assertEqual( 0.5*f2 ,Frac(2,2))     # float*

    self.assertEqual( f2/f1  ,Frac(4,1))     # /frac
    self.assertEqual( f2/2   ,Frac(2,2))     # /int
    self.assertEqual( 2/f2   ,Frac(2,2))     # int/
    self.assertEqual( f1/0.5 ,Frac(2,2))     # /float
    self.assertEqual( 0.5/f1 ,Frac(2,2))     # float/

    self.assertEqual(f2//f1,4) # //frac
    self.assertEqual(f2//2,1) # //int
    self.assertEqual(2//f2,1) # int//
    self.assertEqual(f2//0.5,4) # //float
    self.assertEqual(0.5//f2,0) # float//
    self.assertEqual(f2%f2,0) # %
    self.assertEqual(f2%2,0) # %int
    self.assertEqual(f2%2.0,0) # %float
    self.assertEqual(~f2,f1) # odwrotność
    self.assertEqual(-f2,Frac(-2,1)) # negacja

if __name__=="__main__":
  sys.argv[1:] = [] # usuwam parametry przekazane przez linie komend bo unittest ma jakiś problem
  unittest.main()