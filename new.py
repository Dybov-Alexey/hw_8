from math import sqrt, pi


class point:
    X = 0
    Y = 0
    Z = 0

    def __init__(self,x=0,y=0,z=0):
        self.X = x
        self.Y = y
        self.Z = z

    def distance(self1,self2):
        return sqrt(pow(self2.X-self1.X,2)+pow(self2.Y-self1.Y,2)+pow(self2.Z-self1.Z,2))

        


class quadrangle(point):
    def perimeter(a,b,c):
        A = point.distance(a,b)
        B = point.distance(b,c)
        return (A + B)*2
    
    def area(a,b,c):
        A = point.distance(a,b)
        B = point.distance(b,c)
        return A * B

    def volume(a,b,c,d):
        # C = point.distance(a,d)
        return quadrangle.area(a,b,c) * d


class romb(quadrangle):
    def perimeter(a,b):
        A = point.distance(a,b)
        return 4 * A
    
    def area(a, b, c, d):
        A = point.distance(a,c)
        B = point.distance(b,d)
        return 0.5 * A * B

    def volume(a, b, c, d,C):
        #C = point.distance(a,d)
        return romb.area(a,b,c,d) * C


class triangle(point):
    def perimeter(a,b,c):
        A = point.distance(a,b)
        B = point.distance(b,c)
        C = point.distance(a,c)
        return A + B + C

    def area(a,b,c):
        p = triangle.perimeter(a,b,c)/2
        A = point.distance(a,b)
        B = point.distance(b,c)
        C = point.distance(a,c)
        return sqrt(p*(p-A)*(p-B)*(p-C))

    def volume(a,b,c,d):
        A = point.distance(a,b)
        B = point.distance(b,c)
        C = point.distance(a,c)
        if A != B or B != C:
            print('Для вычисления объема правильной пирамиды нужен правильный треугольник')
            return
        h = sqrt(pow(point.distance(a,d),2) - pow(point.distance(a,c)/2,2))
        return triangle.area(a,b,c)/3*h


class circle(point):
    def long(o,k):
        r = point.distance(o,k)
        return 2*pi*r

    def area(o,k):
        r = point.distance(o,k)
        return pi*r*r

    def volume(o,k):
        r = point.distance(o,k)
        return 4/3*pi*r*r*r