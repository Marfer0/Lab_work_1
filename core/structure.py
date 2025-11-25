class Structure:
    def __init__(self):
        self.warehouses = {}  # словарь: id -> Warehouse
        self.categories = {}  # словарь: id -> Category

    def get_info(self):
        return {
            "склады": {wid: wh.get_info() for wid, wh in self.warehouses.items()},
            "категории": {cid: cat.get_info() for cid, cat in self.categories.items()}
        }

    def add_warehouse(self, warehouse):
        self.warehouses[warehouse.warehouse_id] = warehouse

    def remove_warehouse(self, warehouse_id):
        return self.warehouses.pop(warehouse_id, None)

    def add_category(self, category):
        self.categories[category.category_id] = category

    def remove_category(self, category_id):
        return self.categories.pop(category_id, None)

    def delete(self):
        self.warehouses = {}
        self.categories = {}
