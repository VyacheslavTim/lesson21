from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    def __init__(self, items, capacity):
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, name, amount):
        pass

    @abstractmethod
    def remove(self, name, amount):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
