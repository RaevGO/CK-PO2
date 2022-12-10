import doctest

class BankAccaunt:
    @staticmethod
    def test_values(value) -> None:
        """
        Функция для ValueError и TypeError
        :param value: проверяемый объект
        :return: None or exept
        """
        if not isinstance(value, int):
            if isinstance(value, float):
                if len(str(value)) - str(value).find('.') > 3:
                    raise ValueError('Количество знаков после запятой не может быть больше 2')
                if value < 0:
                    raise ValueError('Значение не может быть меньше 0')
            else:
                raise TypeError('Тип вводимых данных in или float')
        if value < 0:
            raise ValueError('Значение не может быть меньше 0')

    def __init__(self, amount_of_money: float, dept: float) -> None:
        """
        Создание и и подготовка к работе объекта Банковский_Счет
        :param amount_of_money: количество денег на счете
        :param dept: долг на счете

        EX:
        >>> acc = BankAccaunt(100, 10)
        """
        self.test_values(amount_of_money)
        self.test_values(dept)
        self.dept = dept
        self.amount_of_money = amount_of_money

    def add_money(self, contribution: float) -> None:
        """
        Функция, которая добавляет денег на счет

        :param contribution: количество денег, которое хотят добавить
        :return: None

        EX:
        >>> acc = BankAccaunt(100, 10)
        >>> acc.add_money(10)
        """
        self.test_values(contribution)
        self.amount_of_money += contribution

    def get_money(self, amount_charged: float) -> None:
        """
        Снятие денег со счета
        :param amount_charged: Количество денег, которое хотят снять
        :return:None

        :raise ValueError: Если количество денег, которое останется после снятия денег меньше, чем долг, то вызывается ошибка

        EX:
        >>> acc = BankAccaunt(100, 10)
        >>> acc.get_money(25)

        """
        self.test_values(amount_charged)
        if self.amount_of_money - amount_charged < self.dept:
            raise ValueError('Итоговое количество денег не может быть меньше 0')
        self.amount_of_money -= amount_charged

    def pay_the_debt_off(self, contribution: float) -> None:
        """
        Оплачивает часть долга, уменьшая количество денег на счете
        :param contribution: выплата
        :return: None

        :raise ValueError: Если количество денег на счете меньше, чем желаемая оплата, или желаемая выплата больше долга, то выдает ошибку

        EX:
        >>> acc = BankAccaunt(100, 10)
        >>> acc.pay_the_debt_off(5)
        """
        self.test_values(contribution)
        if contribution > self.amount_of_money:
            raise ValueError('Оплата долга не может быть больше количества денег')
        if contribution > self.dept:
            raise ValueError('Оплата долга не может быть больше долга')
        self.amount_of_money -= contribution
        self.dept -= contribution

    def get_info(self) -> tuple:
        """
        Возвращает кортеж из количества денег на счете и размера долга
        :return: Кортеж из количества денег на счете и размера долга

        EX:
        >>> acc = BankAccaunt(100, 50)
        >>> acc.get_info()
        (100, 50)
        """
        return self.amount_of_money, self.dept


if __name__ == '__main__':
    doctest.testmod()
