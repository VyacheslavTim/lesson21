from app.base_class import BaseStorage


class Store(BaseStorage):
    def __init__(self, items, capacity: int = 100):
        super().__init__(items, capacity)
