from core.warehouse import Warehouse
from core.exceptions import WarehouseFullError, ItemNotFoundError

class InventoryManager:
    def __init__(self):
        self.warehouses = []

    def add_warehouse(self, warehouse: Warehouse):
        self.warehouses.append(warehouse)
