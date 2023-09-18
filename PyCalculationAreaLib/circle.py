import math
from typing import Union
from figure import Figure

class Circle(Figure):
    """Класс описывающий круг для подсчета его площади
    Чтобы получить площадь круга ипользуйте:

        circle = Circle(radius).area
    
    Где:
        radius - радиус окружности типа int или float
    """
    def __init__(self,radius: Union[float,int])-> None:
        Circle._CheckRadius(radius)
        self._radius = radius
        self._area = self._get_area()
    
    @property
    def radius(self) -> Union[float,int]:
        return self._radius
    
    @radius.setter
    def radius(self,val) -> None:
        Circle._CheckRadius(val)
        if val != self._radius:
            self._radius = val
            self._area = self._get_area()

    @property
    def area(self) -> Union[float,int]:
        return self._area

    def _get_area(self) -> float:
        return math.pi * self._radius ** 2
    
    def _CheckRadius(radius:Union[float,int]) -> bool:
        if  not type(radius) in (int,float):
            raise ValueError("Радиус должен быть типа int или float")
        if radius <= 0:
            raise ValueError("Радиус должен быть больше нуля") 
        
    
if __name__ == "__main__":
    c = Circle(1)
    print(c.area)