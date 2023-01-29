#Лаба
class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name
    
    @property
    def author(self):
        return self._author
        
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages
    
    @property
    def pages(self):
        return self._pages
    
    @pages.setter
    def pages(self, new_pages):
        if not isinstance(new_pages, int):
            raise TypeError('pages must be int type')
        if new_pages <= 0:
            raise ValueError('pages must be > 0')
        self._pages = new_pages
    
    def __str__(self):
        _str_ = super().__str__()
        return f'{_str_}. Количество страниц {self.pages}'
    
    def __repr__(self):
        _repr_ = super().__repr__()
        return f'{_repr_}, pages={self.pages}'


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
    
    @property
    def duration(self):
        return self._duration
    
    @duration.setter
    def duration(self, new_duration):
        if not isinstance(new_duration, float):
            raise TypeError('duration must be float')
        if new_duration <= 0:
            raise ValueError('duration must be > 0')
        '''
        if (new_duration*60)%1 > 0.01:
            raise ValueError('impossible value in seconds')
        '''#Тут написал проверку на верное введение длительности в переводе на секунды, но оно не будет нормально работать
        self._duration = new_duration    
    
    def __str__(self):
        _str_ = super().__str__()
        return f'{_str_}. Продолжительность {self.duration}'
    
    def __repr__(self):
        _repr_ = super().__repr__()
        return f'{_repr_}, duration={self.duration}'
