from entity.abstract_storage import AbstractStorage
from exceptions import NotEnoughProduct, UnknownProduct, NotEnoughSpace


class BaseStorage(AbstractStorage):

    def __init__(self, items, capacity):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int):

        # Проверяет что место есть
        if self.get_free_space() < amount:
            raise NotEnoughSpace

        # Добавляет товар
        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name: str, amount: int):
        # Проверяет есть ли товар и хватает ли его на складе
        if name not in self.__items:
            raise UnknownProduct
        if self.__items[name] < amount:
            raise NotEnoughProduct

        # Вычесть необходимое кол-во товара, если станет 0 - удалить товар из списка
        self.__capacity -= amount
        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self) -> int:
        # Посчитать сумму значений в __items и вычесть ее из __capacity
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)
