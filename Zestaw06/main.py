import functools,argparse,unittest,sys

# ZADANIE 6.2 (KLASA POINT) 

class Point:
  """Klasa reprezentująca punkty na płaszczyźnie."""
  def __init__(self, x, y):  # konstuktor
    self.x = x
    self.y = y

  def __str__(self): # zwraca string "(x, y)"
    return f'({self.x}, {self.y})'         

  def __repr__(self): # zwraca string "Point(x, y)"
    return f'Point({self.x}, {self.y})'

  def __eq__(self, o): 
    return self.x==o.x and self.y==o.y   # obsługa point1 == point2

  def __ne__(self, other): # obsługa point1 != point2
      return not self == other

  # Punkty jako wektory 2D.
  def __add__(self, o): # v1 + v2
    return Point(self.x+o.x,self.y+o.y)

  def __sub__(self, o): # v1 - v2
    return Point(self.x-o.x,self.y-o.y)

  def __mul__(self, o): # v1 * v2, iloczyn skalarny (liczba)
    return self.x*o.x+self.y*o.y  

  def cross(self, other): # v1 x v2, iloczyn wektorowy 2D (liczba)
      return self.x * other.y - self.y * other.x

  def length(self): # długość wektora
    return (self.x**2+self.y**2)**(1/2) 

  def __hash__(self):
    return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

class TestPoint(unittest.TestCase):
  def test_str(self):
    p = Point(0,0)
    self.assertEqual(str(p),'(0, 0)')

  def test_repr(self):
    p = Point(0,0)
    self.assertEqual(p.__repr__(),'Point(0, 0)')

  def test_compare(self):
    p1 = Point(1,0)
    p2 = Point(1,0)
    p3 = Point(2,0)
    self.assertTrue(p1==p2)
    self.assertFalse(p3==p2)

    self.assertFalse(p1!=p2)
    self.assertTrue(p3!=p2)

  def test_math_operations(self):
    p1 = Point(1,1)
    p2 = Point(2,2)
    self.assertEqual(p1+p2,Point(3,3)) # +
    self.assertEqual(p1-p2,Point(-1,-1)) # -
    self.assertEqual(p1*p2,4) # skalar
    self.assertEqual(p1.cross(p2),0) # wektorowy
    self.assertEqual(p1.length(),2**(1/2)) # dlugosc

  def test_hash(self):
    p = Point(0,0)
    self.assertEqual(p.__hash__(),hash((0,0)))


# END ZADANIE 6.2

# ZADANIE 6.5
class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self): # zwraca "x/y" lub "x" dla y=1
      return f'{self.x}/{self.y}' if self.y!=1 else str(self.x)

    def __repr__(self): # zwraca "Frac(x, y)"
      return f'Frac({self.x}, {self.y})'

    def __eq__(self, o):
      #return (self.x==0 and o.x==0) or (self.x==o.x and self.y==o.y)
      return self.x==o.x and self.y==o.y

    def __ne__(self, o):
      return not self == o

    def __lt__(self, o): # s < o
      return float(self)<float(o)

    def __le__(self, o): # s<= o
      return float(self)<=float(o)

    def __gt__(self, o): # s > o
      return float(self)>float(o)

    def __ge__(self, o): # s >= o
      return float(self)>=float(o)

    def __add__(self, o): # frac1 + frac2
      return Frac(self.x*o.y+o.x*self.y,self.y*o.y)

    def __sub__(self, o): # frac1 - frac2
      return Frac(self.x*o.y-o.x*self.y,self.y*o.y)

    def __mul__(self, o): # frac1 * frac2
      return Frac(self.x*o.x,self.y*o.y)

    def __div__(self, o):  # frac1 / frac2, Python 2
      return Frac(self.x*o.y,self.y*o.x)

    def __truediv__(self, o): # frac1 / frac2, Python 3
      return Frac(self.x*o.y,self.y*o.x)

    def __floordiv__(self, o): # frac1 // frac2, opcjonalnie
      return float(self)//float(o)

    def __mod__(self, o): # frac1 % frac2, opcjonalnie
      return float(self)%float(o)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self): # float(frac)
      return self.x/self.y

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # assert set([2]) == set([2.0])

class TestFrac(unittest.TestCase):
  def test_str(self):
    f = Frac(1,2)
    self.assertEqual(str(f),'1/2')
    self.assertEqual(f.__repr__(),'Frac(1, 2)')

  def test_float(self):
    f = Frac(1,2)
    self.assertEqual(float(f),0.5)

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
    self.assertEqual(f1+f1,Frac(4,4)) # +
    self.assertEqual(f1-f1,Frac(0,4)) # - 
    self.assertEqual(f1*f2,Frac(2,2)) # *
    self.assertEqual(f1*f2,Frac(2,2)) # /
    self.assertEqual(f2//f1,4) # //
    self.assertEqual(f2%f2,0) # %
    self.assertEqual(~f2,f1) # odwrotność
    self.assertEqual(-f2,Frac(-2,1)) # negacja
    

# END ZADANIE 6.5


if __name__=="__main__":
  
  sys.argv[1:] = []
  unittest.main()