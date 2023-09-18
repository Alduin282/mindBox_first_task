import math
from typing import Union
from figure import Figure

class Triangle(Figure):
    """Класс описывающий теугольник для подсчета его площади
    Чтобы получить площадь треугольника ипользуйте:

        triangle = Triangle(a,b,c).area
    
    Где:
        a,b,c - длины сторон треугольника. Тип int или float
    """   
    def __init__(self, a:Union[float,int],b:Union[float,int],c:Union[float,int]) -> None:
        Triangle._CheckSides(a,b,c)
        self._side_lengths = [a,b,c]
        self._side_lengths.sort()
        self._area = self._get_area()
        self._is_right = self._isRight()

    @property
    def area(self) -> Union[float,int]:
        return self._area

    @property
    def side_lengths(self) ->[Union[float,int]]:
        return self._side_lengths
    
    @side_lengths.setter
    def side_lengths(self,val:[Union[float,int]]):
        if len(val) != 3:
            raise ValueError("У треугольника должно быть 3 стороны")
        Triangle._CheckSides(val[0],val[1],val[2])
        val.sort() 
        if not val == self._side_lengths:
            self._side_lengths = val
            self._area = self._get_area()
            self._is_right = self._isRight()
    
    @property
    def is_right(self) -> Union[float,int]:
        return self._is_right

    def change_sides(self,a:Union[float,int],b:Union[float,int],c:Union[float,int])->None:
        Triangle._CheckSides(a,b,c)
        val = [a,b,c]
        val.sort() 
        if not val == self.side_lengths:
            self._side_lengths = val
            self._area = self._get_area()
            self._is_right = self._isRight()

    def _get_area(self)->float:
        p = sum(self._side_lengths)/2
        return math.sqrt(p*(p-self._side_lengths[0])*(p-self._side_lengths[1])*(p-self._side_lengths[2]))
    
    def _isRight(self)->bool:
        return self._side_lengths[0]**2 + self._side_lengths[1]**2 == self._side_lengths[2]**2
    
    def _CheckSides(a:Union[float,int],b:Union[float,int],c:Union[float,int]):
        if not type(a) in (int,float) or not type(b) in (int,float)  or not type(c) in (int,float):
            raise ValueError("Стороны треугольника должны быть типа int, float")
        if a<=0 or b<=0 or c<=0:
            raise ValueError("Стороны треугольника должны быть больше нуля")
        if a>(b+c) or b>(a+c) or c>(a+b):
            raise ValueError("Такого треугольника не существует") 
        
if __name__ == "__main__":
    t = Triangle(5,4,3)
    print(t.area)