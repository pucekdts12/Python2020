import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random


class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  @staticmethod
  def createRandom():
    return Point(random.randint(0,1000),random.randint(0,1000))

  def __repr__(self):
    return f'({self.x},{self.y})'


class Rectangle:
  def __init__(self,x,y,w,h):
    self.x=x
    self.y=y
    self.h=h
    self.w=w

def render(points,r):
  fig,ax=plt.subplots(1)
  for p in points:
    plt.plot(p.x,p.y,'x')
  rect = patches.Rectangle((r.x,r.y),r.w,r.h,linewidth=1,edgecolor='r',facecolor='none',zorder=10)
  ax.add_patch(rect)
  plt.show()


def closestX(points,start_ind,end_coord):
  for i in range(start_ind,len(points)):
    if points[i].x>end_coord:
      return (i-1 if i-1 > start_ind else start_ind)
  return len(points)-1

def closestY(points,start_ind,end_coord):
  for i in range(start_ind,len(points)):
    if points[i].y>end_coord:
      return (i-1 if i-1 > start_ind else start_ind)
  return len(points)-1

def bruteForce(points,rect):
  pointsX = sorted(points,key=lambda p:p.x)
  max = 0
  for i,sx in enumerate(pointsX):
    ex = closestX(pointsX,i,sx.x + rect.w)
    pointsY = sorted(pointsX[i:ex],key=lambda p:p.y)
    for j,sy in enumerate(pointsY):
      ey = closestY(pointsY,j,sy.y + rect.h)
      pp = pointsY[j:ey]
      # print(pp)
      if len(pp)>max:
        max = len(pp)
        rect.x = sx.x
        rect.y = sy.y
      
  
  

  print(f"Max is {max}")
  return rect




"""
  Sprobowac QuadTree



"""

random.seed(100)

points = [ Point.createRandom() for i in range(0,100) ]
rect = Rectangle(0,0,100,100)


rect = bruteForce(points,rect)

render(points,rect)






    









