'''
Многие операторы делаются +- одинаково, поэтому тут грубо говоря каждого вида
'''
class overload:
    X = 0
    Y = 0
    Z = 0

    def __init__(self,x=0,y=0,z=0):
        self.X = x
        self.Y = y
        self.Z = z

    def print_point(self):
        print(f'Координата X = {self.X}\nКоордината Y = {self.Y}\nКоордината Z = {self.Z}')

    def __add__(self,other):
        return overload(self.X + other.X, self.Y + other.Y, self.Z + other.Z)
    
    def __sub__(self,other):
        return overload(self.X - other.X, self.Y - other.Y, self.Z - other.Z)
    
    def __gt__(self, other):
        if self.X > other.X and self.Y > other.Y and self.Z > other.Z:
            return True
        else:
            return False
    
    def __lt__(self, other):
        if self.X < other.X and self.Y < other.Y and self.Z < other.Z:
            return True
        else:
            return False

    def __isub__(self, other):
        self.X -= other.X
        self.Y -= other.Y
        self.Z -= other.Z
        return self

    def __lshift__(self, other):
        self.X << other
        self.Y << other
        self.Z << other
        return self

    def __mul__(self,b):
        return overload(self.X / b, self.Y / b, self.Z / b)


print('''Введите координаты центра и точки лежащей на окружности в трехмерном пространстве''')
q,w,e = input('Введите x y z через пробел ').split()
q, w , e = int(q),int(w),int(e)
pt1 = overload(q,w,e)
q,w,e = input('Введите x y z через пробел ').split()
q, w , e = int(q),int(w),int(e)
pt2 = overload(q,w,e)
print('\nНовая точка при сложении координат - ')
overload.print_point(pt1+pt2)
print('\nНовая значение первой точки - ')
pt1 -= pt2
overload.print_point(pt1)
print('\nНовая точка при сложении координат - ')
overload.print_point(pt1+pt2)
print(f'\nПервая точка > вторая точка: {pt1>pt2}')
print(f'\nПервая точка < вторая точка: {pt1<pt2}\n')
pt3 = pt1 << 1
print('Битовый сдвиг влево')
overload.print_point(pt3)
print('\nВыполняем умножение, а оно делит')
b = 4
overload.print_point(pt3*b)
        