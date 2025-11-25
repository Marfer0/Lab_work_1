class Structure:
    def __init__(self):
        self.warehouses = {}  # словарь: id -> Warehouse
        self.categories = {}  # словарь: id -> Category

    def get_info(self):
        return {
            "склады": {wid: wh.get_info() for wid, wh in self.warehouses.items()},
            "категории": {cid: cat.get_info() for cid, cat in self.categories.items()}
        }
