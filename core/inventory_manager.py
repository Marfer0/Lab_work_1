from core.warehouse import Warehouse
from core.exceptions import WarehouseFullError, ItemNotFoundError

class InventoryManager:
    def __init__(self):
        self.warehouses = []

    def add_warehouse(self, warehouse: Warehouse):
        self.warehouses.append(warehouse)

    def move_item(self, item_id, source_id, target_id):
        source = next((w for w in self.warehouses if w.warehouse_id == source_id), None)
        target = next((w for w in self.warehouses if w.warehouse_id == target_id), None)
        if not source or not target:
            raise ValueError("Неверный идентификатор склада")

        item = source.remove_item(item_id)
        try:
            target.add_item(item)
        except WarehouseFullError as e:
            source.add_item(item)
            raise e

    def find_item(self, item_id):
        for wh in self.warehouses:
            try:
                return wh.get_item(item_id)
            except ItemNotFoundError:
                continue
        raise ItemNotFoundError(f"Товар {item_id} не найден ни на одном складе")