import doctest

class Tea:
    @staticmethod
    def test_values(value) -> None:
        """
        Функция для ValueError и TypeError
        :param value: проверяемый объект
        :return: None or exept
        """
        if not isinstance(value, (float, int)):
            raise TypeError('Тип вводимых данных должен быть int или float')

    def __init__(self, temperature: float, total: float):
        """
        Создание и подготовка к работе объекта Чай
        :param temperature: Температура чая
        :param total: Количество чая(может быть очень большим)

        :raise ValueError: Если температура больше 100 градусов или меньше или равна 0, то вызывает ошибку
        :raise ValueError: Если объем меньше 0, что вызывает ошибку

        EX:
        >>> tea = Tea(20, 10)
        """
        self.test_values(temperature)
        self.test_values(total)
        if temperature <= 0:
            raise ValueError('Температура не может быть отрицательной')
        if total < 0:
            raise ValueError('Объем не может быть меньше 0')
        if temperature > 100:
            raise ValueError('Температура не может быть больше 100 градусов')
        self.temperature = temperature
        self.total = total

    def heat(self, up: float) -> None:
        """
        Нагрев чая
        :param up: количество градусов на которое нагревают чай
        :return: None

        :raise ValueError: Если итоговая температура больше 100 градусов, или нагрев меньше 0, то вызывает ошибку

        EX:
        >>> tea = Tea(20, 10)
        >>> tea.heat(20)
        """
        self.test_values(up)
        if up < 0:
            raise ValueError('Нельзя остудить чай')
        if self.temperature + up > 100:
            raise ValueError('Итоговая температура не может быть больше 100 градусов')
        self.temperature += up

    def drink(self, volume: float) -> None:
        """
        Выпивает часть чая
        :param volume: Количество, которое выпивает
        :return: None

        :raise ValueError: Если выпиваемый объем меньше 0 или больше реального объема, то вызывает ошибку

        EX:
        >>> tea = Tea(80, 40)
        >>> tea.drink(20)
        """
        self.test_values(volume)
        if volume < 0:
            raise ValueError('Объем не может быть меньше 0')
        if volume > self.total:
            raise ValueError('Объем не может быть больше реального объема')
        self.total -= volume

    def make_more(self, volume: float) -> None:
        """
        Добавляет введенный объем к реальному
        :param volume: Количество, которое добавляется
        :return: None

        :raise ValueError: Если объем меньше 0, то выдает ошибку

        EX:
        >>> tea = Tea(20, 100)
        >>> tea.make_more(20)
        """
        self.test_values(volume)
        if volume < 0:
            raise ValueError('Объем не может быть меньше 0')
        self.total += volume

    def get_info(self) -> tuple:
        """
        Возвращает кортеж из температуры и реального объема
        :return: Кортеж из температуры и реального объема

        EX:
        >>> tea = Tea(100, 50)
        >>> tea.get_info()
        (100, 50)
        """
        return self.temperature, self.total


if __name__ == '__main__':
    doctest.testmod()
