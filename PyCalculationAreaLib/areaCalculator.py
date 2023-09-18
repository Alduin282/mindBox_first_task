from figure import Figure

class AreaCalculator():
    """Класс для подсчета площади фигуры произвольного типа
    Чтобы получить площадь ипользуйте:

        area = AreaCalculator(figure).area
        ИЛИ
        area = AreaCalculator.get_area(figure)
    
    Где:
        figure - объект типа Figure
    """ 
    def __init__(self,figure:Figure) -> None:
        if not isinstance(figure,Figure):
            raise ValueError("Не верный тип фигуры")
        self._area = figure.area
    
    @property
    def area(self):
        return self._area
    
    def get_area(figure:Figure) -> float:
        if not isinstance(figure,Figure):
            raise ValueError("Не верный тип фигуры")
        return figure.area