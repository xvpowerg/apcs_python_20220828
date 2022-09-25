class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      c_n = self.__class__.__name__
      print(c_n, self, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
pt4 = Point()
print (id(pt1), id(pt2), id(pt3), id(pt4))
del pt1
print (id(pt2), id(pt3), id(pt4))
del pt2
print (id(pt3), id(pt4))
del pt3
print (id(pt4))
del pt4
