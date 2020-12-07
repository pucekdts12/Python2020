import sys,math
from points import Point

class Circle:
  """Klasa reprezentująca okręgi na płaszczyźnie."""
  def __init__(self, x, y, r):
    if r < 0:
      raise ValueError("promień ujemny")
    self.pt = Point(x, y)
    self.r = r

  def __repr__(self): return f'Circle{self.pt.x, self.pt.y, self.r}'     # "Circle(x, y, radius)"

  def __eq__(self, o):
    return self.pt == o.pt and self.r == o.r

  def __ne__(self, o):
    return not self == o

  def area(self): return math.pi*self.r**2       # pole powierzchni

  def move(self, x, y): self.pt+=Point(x,y) # przesuniecie o (x, y)

  def cover(self, o): # najmniejszy okrąg pokrywający oba
    nc = Point((self.pt.x+o.pt.x)/2,(self.pt.y+o.pt.y)/2)
    nr = (nc-o.pt).length()+max(self.r,o.r)
    return Circle(nc.x, nc.y, nr)

# Kod testujący moduł.

import unittest

class TestCircle(unittest.TestCase):
  def test_str(self):
    c = Circle(1,2,5)
    self.assertEqual(repr(c),'Circle(1, 2, 5)')

  def test_exceptions(self):
    with self.assertRaises(ValueError):
      c = Circle(1,2,-6)


  def test_compare(self):
    c1 = Circle(0,0,5)
    c2 = Circle(0,0,5)
    c3 = Circle(1,2,5)

    self.assertTrue(c1==c2)
    self.assertFalse(c1!=c2)
    self.assertFalse(c3==c2)
    self.assertTrue(c3!=c2)


  def test_operations(self):
    c1 = Circle(0,0,5)
    c2 = Circle(3,0,1)
    c1.move(1,2)
    self.assertTrue(c1==Circle(1,2,5))
    self.assertTrue(c1.area()==(math.pi*5**2))
    self.assertTrue(c1.cover(c1)==c1)
    self.assertTrue(c1.cover(c2)==Circle(2,1,(2**(1/2)+5)))

if __name__=="__main__":
  sys.argv[1:] = [] # usuwam parametry przekazane przez linie komend bo unittest ma jakiś problem
  unittest.main()