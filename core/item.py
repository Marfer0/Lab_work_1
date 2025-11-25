class Item:
    def __init__(self, item_id, name, quantity, unit, category):
        if quantity < 0:
            raise ValueError(f"Количество для {name} не может быть отрицательным")
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.category = category
    def get_info(self):
        return {
            "id": self.item_id,
            "название": self.name,
            "количество": self.quantity,
            "единица": self.unit,
            "категория": self.category
        }
    def update_name(self, new_name):
        self.name = new_name

    def update_quantity(self, new_quantity):
        if new_quantity < 0:
            raise ValueError(f"Количество для {self.name} не может быть отрицательным")
        self.quantity = new_quantity

    def update_unit(self, new_unit):
        self.unit = new_unit

    def update_category(self, new_category):
        self.category = new_category
    def delete(self):
        self.item_id = None
        self.name = None
        self.quantity = 0
        self.unit = None
        self.category = None

    def __repr__(self):
        return f"{self.name} — {self.quantity} {self.unit}, категория: {self.category}"