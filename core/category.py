class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name

    def get_info(self):
        return {
            "id": self.category_id,
            "название": self.name
        }