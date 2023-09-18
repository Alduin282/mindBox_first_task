# Калькулятор площадей #
## Использование ##
Создание фигур и взятие площади: <br />
Треугольник: 
>    #треугольник (длины сторон) <br />
>    t = t.Triangle(5,4,3)  <br />
>    #площадь  <br />
>    print(t.area) #6.0  <br />
    
Круг:
>    #круг (радиус) <br />
>    c = c.Circle(1) <br />
>    #площадь <br />
>    print(c.area) #3.141593 <br />

Любая фигура:
>    #площадь круга <br />
>    area = AreaCalculator.get_area(Circle(5)) <br />
>    #площадь треугольника <br />
>    area = AreaCalculator.get_area(Triangle(4,3,5)) <br />
