class Item:
    def __init__(self, item_id, name, quantity, unit, category):
        if quantity < 0:
            raise ValueError(f"Количество для {name} не может быть отрицательным")
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.category = category