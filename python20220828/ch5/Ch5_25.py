class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        print("self_mag ="+str(self_mag))
        other_mag = (other.x ** 2) + (other.y ** 2)
        print("other_mag ="+str(other_mag))
        return self_mag < other_mag

print(Point(1,1) < Point(-2,-3))
