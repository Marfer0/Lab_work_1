class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name

    def get_info(self):
        return {
            "id": self.category_id,
            "название": self.name
        }
    def update_name(self, new_name):
        self.name = new_name

    def delete(self):
        self.category_id = None
        self.name = None

    def __repr__(self):
        return f"Категория: {self.name}"
