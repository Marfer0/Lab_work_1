class Supplier:
    def __init__(self, supplier_id, name):
        self.supplier_id = supplier_id
        self.name = name

    def get_info(self):
        return {
            "id": self.supplier_id,
            "название": self.name
        }
    def update_name(self, new_name):
        self.name = new_name

    def supply_item(self, warehouse, item):
        try:
            warehouse.add_item(item)
        except Exception as e:
            print(f"Ошибка поставки {item.name} на склад {warehouse.name}: {e}")


    def delete(self):
        self.supplier_id = None
        self.name = None

    def __repr__(self):
        return f"Поставщик: {self.name}"