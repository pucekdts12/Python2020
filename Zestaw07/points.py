import functools,argparse,unittest,sys

class Point:
  def __init__(self, x, y):  # konstuktor
    self.x = x
    self.y = y

  def __str__(self):        return f'({self.x}, {self.y})'         
  def __repr__(self):       return f'Point({self.x}, {self.y})'
  def __eq__(self, o):      return self.x==o.x and self.y==o.y   # obsługa point1 == point2
  def __ne__(self, other):  return not self == other
  def __add__(self, o):     return Point(self.x+o.x,self.y+o.y)
  def __sub__(self, o):     return Point(self.x-o.x,self.y-o.y)
  def __mul__(self, o):     return self.x*o.x+self.y*o.y  
  def cross(self, other):   return self.x * other.y - self.y * other.x
  def length(self):         return (self.x**2+self.y**2)**(1/2) 
  def __hash__(self):       return hash((self.x, self.y))   # bazujemy na tuple, immutable points