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