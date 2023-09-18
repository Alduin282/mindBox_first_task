# Калькулятор площадей #
## Использование ##
Создание фигур и взятие площади:
    Треугольник: 
        #треугольник (длины сторон)
        t = t.Triangle(5,4,3)
        #площадь
        print(t.area) #6.0
    
    Круг:
        #круг (радиус)
        c = c.Circle(1)
        #площадь
        print(c.area) #3.141593

    Любая фигура:
        #площадь круга
        area = AreaCalculator.get_area(Circle(5))
        #площадь треугольника
        area = AreaCalculator.get_area(Triangle(4,3,5))
