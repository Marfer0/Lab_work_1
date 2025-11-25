class Section:
    def __init__(self, section_id, name, capacity):
        self.section_id = section_id
        self.name = name
        self.capacity = capacity
        self.items = []

    def get_info(self):
        return {
            "id": self.section_id,
            "название": self.name,
            "вместимость": self.capacity,
            "товары": [item.get_info() for item in self.items]
        }
    def add_item(self, item):
        total_qty = sum(i.quantity for i in self.items)
        if total_qty + item.quantity > self.capacity:
            raise ValueError(f"Невозможно добавить {item.name}, секция '{self.name}' переполнена")
        self.items.append(item)

    def remove_item(self, item_id):
        for i, item in enumerate(self.items):
            if item.item_id == item_id:
                return self.items.pop(i)
        raise ValueError(f"Товар с id {item_id} не найден в секции '{self.name}'")

    def get_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        raise ValueError(f"Товар с id {item_id} не найден в секции '{self.name}'")