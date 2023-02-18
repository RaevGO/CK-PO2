import math
import doctest

class Function:
    def __init__(self, eq : str, x : float):
        '''
        Создание и подготовка к работе объекта Function
        :param eq: выражение
        :param x: значение параметра x

        EX:
        >>> f = Function('5*x + 10', 2)
        '''
        self.eq = eq
        self.x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        if not (isinstance(new_x, int) or isinstance(new_x, float)):
            raise TypeError('x must me int or float')
        self._x = new_x

    def __str__(self) -> str:
        return f'Уравнение {self.eq}. x = {self.x}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(eq={self.eq}, x={self.x})'

    def substitution(self) -> float:
        '''
        Возвращает значение выражения при данном x
        :return: float

        :raise SyntaxError: неверное написание выражения

        EX:
        >>> f = Function('5*x + 10', 2)
        >>> f.substitution()
        20
        '''
        return eval(self.eq,{'x':self.x})

class Equation(Function):
    def __init__(self, eq : str, x : float, type_ : str):
        '''
        Создание и подготовка к работе объекта Function
        :param eq: наследуется из Function
        :param type_: тип уравнения
        :param x: наследуется из Function

        EX:
        >>> f = Equation('5*x + 10', 3, 'linear')
        '''
        super(Equation, self).__init__(eq, x)
        self.type_ = type_

    @property
    def type_(self):
        return self._type_

    @type_.setter
    def type_(self, new_type):
        if not (new_type == 'linear' or new_type == 'quadratic'):
            raise ValueError('type must me "linear" or "quadratic"')
        self._type_ = new_type

    def __str__(self) -> str:
        _str_ = super().__str__()
        return f'{_str_}. Тип уравнения: {self.type_}'

    def __repr__(self) -> str:
        _repr_ = super().__repr__()
        return f'{_repr_}, type_={self.type_}'

    def solve(self) -> (float, [float, float]):
        '''
        Возвращает решение уравнения
        :return: Список или одиночное значение решения

        :raise SyntaxError: Неверное написание выражения

        EX:
        >>> f = Equation('5*x + 10', 3, 'linear')
        >>> f.solve()
        -2.0
        '''
        if self.type_ == 'linear':
            try:
                ans = -float(self.eq[self.eq.find('x') + 1:].replace(' ', '')) / float(self.eq[:self.eq.find('x') - 1])
            except Exception:
                raise SyntaxError("print eq like: a*x +- b. Don't use: b < 0, ()")
            return ans
        else:
            try:
                a = float(self.eq[:self.eq.find('**') - 2])
                b = float(self.eq[self.eq.find('**') + 3:self.eq.find('*x ')].replace(' ', ''))
                c = float((self.eq[self.eq.find('*x ') + 2:].replace(' ', '')))
            except Exception:
                raise SyntaxError("print eq like: a*x**2 +- b*x +- c. Don't use: b or c < 0, () ")
            if b**2 - 4*a*c < 0:
                print('No solution in R')
                return []
            return [(-b + math.sqrt(b**2 - 4*a*c)) / (2*a), (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)]

if __name__ == '__main__':
    doctest.testmod()


