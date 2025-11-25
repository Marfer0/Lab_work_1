class StockTransfer:
    def __init__(self, manager, item_id, source_id, target_id):
        self.manager = manager
        self.item_id = item_id
        self.source_id = source_id
        self.target_id = target_id
        self.success = False

    def get_info(self):
        return {
            "item_id": self.item_id,
            "source": self.source_id,
            "target": self.target_id,
            "успешно": self.success
        }
    def execute_transfer(self):
        try:
            self.manager.move_item(self.item_id, self.source_id, self.target_id)
            self.success = True
        except Exception as e:
            self.success = False
            raise e

    def rollback(self):
        if self.success:
            self.manager.move_item(self.item_id, self.target_id, self.source_id)
            self.success = False

    def delete(self):
        self.manager = None
        self.item_id = None
        self.source_id = None
        self.target_id = None
        self.success = False