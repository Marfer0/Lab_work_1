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