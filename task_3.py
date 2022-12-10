import doctest
import math

class Car:
    @staticmethod
    def test_value(value):
        """
        Функция для ValueError и TypeError
        :param value: проверяемый объект
        :return: None or exept
        """
        if not isinstance(value, (float, int)):
            raise TypeError('Тип вводимых данных должен быть int или float')
        if value <= 0:
            raise ValueError('Значение не может быть меньше или равно 0')

    def __init__(self, volum_tank: float, amoun_petrol: float, consumption: float):
        """
        Создание и подготовка к работе объекта Машина
        :param volum_tank: Объем бака
        :param amoun_petrol: Количество бензина в баке
        :param consumption: Расход

        EX:
        >>> car = Car(20, 5, 1)
        """
        self.test_value(volum_tank)
        self.test_value(amoun_petrol)
        self.test_value(consumption)
        if volum_tank < amoun_petrol:
            raise ValueError('Объем бака не может быть меньше объема бензина')
        self.consumption = consumption
        self.volum_tank = volum_tank
        self.amoun_petrol = amoun_petrol

    def can_i_get_there(self, distance, drive=False) -> bool:
        """
        Возращает True, если топлива хватит на дистанцию и False, если нет
        :param distance: Дистанция, которую нужно проехать
        :param drive: Нужно ли проезжать дистанцию сейчас
        :return: Сможет ли проехать distance

        EX:
        >>> car = Car(20, 10, 1)
        >>> car.can_i_get_there(5)
        True
        >>> car.can_i_get_there(5, True)
        Осталось 5.0 топлива
        True


        """
        self.test_value(distance)
        if not isinstance(drive, bool):
            raise  TypeError('Тип данных drive - bool')
        if distance/self.consumption > self.volum_tank:
            return False, print(f'С вашим объемом бака вам потребуется дозаправка минимум {math.ceil(distance/self.volum_tank - 1)} раз(а)')
        if distance/self.consumption > self.amoun_petrol:
            return False, print(f'Вам не хватает {self.amoun_petrol - distance/self.consumption} топлива')
        if drive:
            self.amoun_petrol -= distance/self.consumption
            print(f'Осталось {self.amoun_petrol} топлива')
            return True
        return True

    def add_petrol(self, volume: float) -> None:
        """
        Добавляет топливо в бак
        :param volume: Количество топлива для добавления
        :return: None

        :raise ValueError: Если итоговое количество топлива больше объема бака, то выдает ошибку

        EX:
        >>> car = Car(20, 10, 2)
        >>> car.add_petrol(6)
        """
        self.test_value(volume)
        if self.amoun_petrol + volume > self.volum_tank:
            raise ValueError('Итоговое значение количества топлива не может быть больше объема бака')

    def get_info(self) -> tuple:
        """
        Возвращает кортеж из объема бака, количества топлива и расхода
        :return: Кортеж из объема бака, количества топлива и расхода

         EX:
        >>> car = Car(100, 50, 2)
        >>> car.get_info()
        (100, 50, 2)
        """
        return self.volum_tank, self.amoun_petrol, self.consumption

if __name__ == '__main__':
    doctest.testmod()