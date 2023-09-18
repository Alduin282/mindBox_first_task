from abc import ABC, abstractproperty , abstractmethod
from typing import Union

class Figure(ABC):
    """Абстрактный класс Figure. Наследуется для создания фигуры с 
    возможностью подсчета площади.
    """
   
    @abstractmethod
    def _get_area(self) -> Union[float,int]:
        pass
    
    @abstractproperty
    def area(self) ->Union[float,int]:
        pass