from core.item import Item
from core.exceptions import WarehouseFullError, ItemNotFoundError

class Warehouse:
    def __init__(self, warehouse_id, name, capacity):
        self.warehouse_id = warehouse_id
        self.name = name
        self.capacity = capacity
        self.items = []

    def get_info(self):
        return {
            "id": self.warehouse_id,
            "название": self.name,
            "вместимость": self.capacity,
            "товары": [item.get_info() for item in self.items]
        }