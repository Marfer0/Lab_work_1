class Supplier:
    def __init__(self, supplier_id, name):
        self.supplier_id = supplier_id
        self.name = name

    def get_info(self):
        return {
            "id": self.supplier_id,
            "название": self.name
        }
