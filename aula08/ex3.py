class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        

class Circle():

    def __init__(self,radius,center):
        self.radius=radius
        self.center=center
ponto=Point(150,100)
c1=Circle(75,ponto)
print(c1.center)
#def point_in_circle(circle,point):
    