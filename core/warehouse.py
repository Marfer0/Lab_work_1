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
    def add_item(self, item: Item):
        total_qty = sum(i.quantity for i in self.items)
        if total_qty + item.quantity > self.capacity:
            raise WarehouseFullError(f"Невозможно добавить {item.name}, склад '{self.name}' переполнен")
        self.items.append(item)

    def remove_item(self, item_id):
        for i, item in enumerate(self.items):
            if item.item_id == item_id:
                return self.items.pop(i)
        raise ItemNotFoundError(f"Товар с id {item_id} не найден на складе '{self.name}'")

    def get_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        raise ItemNotFoundError(f"Товар с id {item_id} не найден на складе '{self.name}'")