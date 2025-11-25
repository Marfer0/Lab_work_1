class ReportService:

    @staticmethod
    def log(message):
        print(message)

    @staticmethod
    def generate_full_report(warehouses, sections=None, categories=None, suppliers=None, transfers=None):
        print("\n=== Полный отчёт по всем классам ===\n")
        for wh in warehouses:
            print(f"Склад '{wh.name}' (ID: {wh.warehouse_id}, вместимость: {wh.capacity})")
            for item in wh.items:
                print(f"  - {item.get_info()}")
            print()
        if sections:
            for sec in sections:
                print(f"Секция '{sec.name}' (ID: {sec.section_id}, вместимость: {sec.capacity})")
                for item in sec.items:
                    print(f"  - {item.get_info()}")
                print()
        if categories:
            print("Категории товаров:")
            for cat in categories:
                print(f"  - {cat.get_info()}")
            print()
        if suppliers:
            print("Поставщики:")
            for sup in suppliers:
                print(f"  - {sup.get_info()}")
            print()
        if transfers:
            print("Перемещения товаров (StockTransfer):")
            for tr in transfers:
                print(f"  - {tr.get_info()}")
            print()
