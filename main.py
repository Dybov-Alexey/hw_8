from new import *
import os


while True:
    os.system("cls")
    n = input('''
    Выберете:
    1. Прямоугльник/прямоугольный параллелепипед
    2. Ромб/параллелепипед с прямоугольным основанием
    3. Треугольник/правильная пирамида
    4. Круг/шар
    Пустой ввод - выход.
    ''')
    if n == '1':
        pt1 = 0
        while True:
            os.system("cls")
            n = input('''
            Выберете:
            1. Периметр
            2. Площадь
            3. Объем прямоугльного параллелепипед
            4. Выход
            ''')
            try:
                if n == '1':
                    if not pt1:
                        print('''Введите координаты трех вершин прямоугольника в трехмерном пространстве ''')
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt1 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt2 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt3 = point(q,w,e)
                    print(f'Периметр прямоугольника равен {quadrangle.perimeter(pt1,pt2,pt3)}')
                    input('Для продолженя нажмите enter')
                if n == '2':
                    if not pt1:
                        print('''Введите координаты трех вершин прямоугольника в трехмерном пространстве ''')
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt1 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt2 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt3 = point(q,w,e)
                    print(f'Площадь прямоугольника равна {quadrangle.area(pt1,pt2,pt3)}')
                    input('Для продолженя нажмите enter')
                if n == '3':
                    if not pt1:
                        print('''Введите координаты трех вершин прямоугольника в трехмерном пространстве ''')
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt1 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt2 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt3 = point(q,w,e)
                    h = input('Введите высоту ')
                    print(f'Объем параллелепипеда равен {quadrangle.volume(pt1,pt2,pt3,h)}')
                    input('Для продолженя нажмите enter')
                if n == '4':
                    break
            except:
                print('Неверный символ!')
                input('Для продолженя нажмите enter')
                break
    if n == '2':
        pt1 = 0
        while True:
            os.system("cls")
            n = input('''
            Выберете:
            1. Периметр
            2. Площадь
            3. Объем прямоугльного параллелепипед
            4. Выход
            ''')
            try:
                if n == '1':
                    if not pt1:
                        print('''Введите координаты четырех вершин ромба в трехмерном пространстве ''')
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt1 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt2 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt3 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt4 = point(q,w,e)
                    print(f'Периметр ромба равен {romb.perimeter(pt1,pt2)}')
                    input('Для продолженя нажмите enter')
                if n == '2':
                    if not pt1:
                        print('''Введите координаты четырех вершин прямоугольника в трехмерном пространстве ''')
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt1 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt2 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt3 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt4 = point(q,w,e)
                    print(f'Площадь ромба равна {romb.area(pt1,pt2,pt3,pt4)}')
                    input('Для продолженя нажмите enter')
                if n == '3':
                    if not pt1:
                        print('''Введите координаты четырех вершин прямоугольника в трехмерном пространстве ''')
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt1 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt2 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt3 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt4 = point(q,w,e)
                    h = input('Введите высоту ')
                    h = int(h)
                    print(f'Объем параллелепипеда с боковой стороной ромб равен {romb.volume(pt1,pt2,pt3,pt4,h)}')
                    input('Для продолженя нажмите enter')
                if n == '4':
                    break
            except:
                print('Неверный символ!')
                input('Для продолженя нажмите enter')
                break
    if n == '3':
        pt1 = 0
        while True:
            os.system("cls")
            n = input('''
            Выберете:
            1. Периметр
            2. Площадь
            3. Объем правильной пирамиды
            4. Выход
            ''')
            try:
                if n == '1':
                    if not pt1:
                        print('''Введите координаты четырех вершин ромба в трехмерном пространстве ''')
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt1 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt2 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt3 = point(q,w,e)
                    print(f'Периметр треугольника равен {triangle.perimeter(pt1,pt2,pt3)}')
                    input('Для продолженя нажмите enter')
                if n == '2':
                    if not pt1:
                        print('''Введите координаты четырех вершин прямоугольника в трехмерном пространстве ''')
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt1 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt2 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt3 = point(q,w,e)
                    print(f'Площадь треугольника равна {triangle.area(pt1,pt2,pt3)}')
                    input('Для продолженя нажмите enter')
                if n == '3':
                    if not pt1:
                        print('''Введите координаты четырех вершин прямоугольника в трехмерном пространстве ''')
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt1 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt2 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt3 = point(q,w,e)
                    h = input('Введите высоту ')
                    h = int(h)
                    print(f'Объем правильной пирамиды равен {triangle.volume(pt1,pt2,pt3,h)}')
                    input('Для продолженя нажмите enter')
                if n == '4':
                    break
            except:
                print('Неверный символ!')
                input('Для продолженя нажмите enter')
                break
    if n == '4':
        pt1 = 0
        while True:
            os.system("cls")
            n = input('''
            Выберете:
            1. Периметр
            2. Площадь
            3. Объем шара
            4. Выход
            ''')
            try:
                if n == '1':
                    if not pt1:
                        print('''Введите координаты центра и точки лежащей на окружности в трехмерном пространстве ''')
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt1 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt2 = point(q,w,e)
                    print(f'Периметр круга равен {circle.long(pt1,pt2)}')
                    input('Для продолженя нажмите enter')
                if n == '2':
                    if not pt1:
                        print('''Введите координаты центра и точки лежащей на окружности в трехмерном пространстве''')
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt1 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt2 = point(q,w,e)
                    print(f'Площадь круга равна {circle.area(pt1,pt2)}')
                    input('Для продолженя нажмите enter')
                if n == '3':
                    if not pt1:
                        print('''Введите координаты центра и точки лежащей на окружности в трехмерном пространстве ''')
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt1 = point(q,w,e)
                        q,w,e = input('Введите x y z через пробел ').split()
                        q, w , e = int(q),int(w),int(e)
                        pt2 = point(q,w,e)
                    print(f'Объем шара равен {circle.volume(pt1,pt2)}')
                    input('Для продолженя нажмите enter')
                if n == '4':
                    break
            except:
                print('Неверный символ!')
                input('Для продолженя нажмите enter')
                break         
    if n == '':
        break
