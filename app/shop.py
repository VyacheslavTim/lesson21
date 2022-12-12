from app.base_class import BaseStorage
from exception import HugeAmountProduct


class Shop(BaseStorage):
    def __init__(self, items, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name, amount):
        if self.get_unigue_items_count() >= 5:
            raise HugeAmountProduct
        super().add(name, amount)
