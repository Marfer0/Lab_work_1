from core.item import Item, PerishableItem
from core.category import Category
from core.warehouse import Warehouse
from core.section import Section
from core.inventory_manager import InventoryManager
from core.supplier import Supplier
from core.structure import Structure
from core.stock_transfer import StockTransfer
from services.file_manager import FileManager
from services.report_service import ReportService

def main():
    ReportService.log("=== Запуск программы: создание объектов ===")

    item1 = Item(101, "Саморезы", 30, "шт.", "Строительные материалы")
    item2 = PerishableItem(102, "Молоко", 20, "л", "Продукты", "2025-12-31")
    item3 = Item(103, "Краска", 15, "л", "Строительные материалы")
    item4 = PerishableItem(104, "Йогурт", 20, "шт.", "Продукты", "2025-11-30")

    ReportService.log(f"Созданы товары: {item1.name}, {item2.name}, {item3.name}, {item4.name}")

    cat1 = Category(1, "Строительные материалы")
    cat2 = Category(2, "Продукты")
    cat3 = Category(3, "Химия")
    ReportService.log(f"Созданы категории: {cat1.name}, {cat2.name}, {cat3.name}")

    wh1 = Warehouse(1, "Главный склад", 100)
    wh2 = Warehouse(2, "Второй склад", 100)
    wh3 = Warehouse(3, "Третий склад", 80)
    ReportService.log(f"Созданы склады: {wh1.name}, {wh2.name}, {wh3.name}")

    wh1.add_item(item1)
    wh1.add_item(item3)
    wh2.add_item(item2)
    wh3.add_item(item4)

    section1 = Section(1, "Секция А", 50)
    section2 = Section(2, "Секция Б", 60)
    section1.add_item(item1)
    section2.add_item(item2)

    supplier1 = Supplier(1, "Лучший поставщик")
    supplier2 = Supplier(2, "Поставщик №2")
    ReportService.log(f"Созданы поставщики: {supplier1.name}, {supplier2.name}")

    inv_manager = InventoryManager()
    inv_manager.add_warehouse(wh1)
    inv_manager.add_warehouse(wh2)
    inv_manager.add_warehouse(wh3)

    transfer1 = StockTransfer(inv_manager, 101, 1, 2)
    transfer2 = StockTransfer(inv_manager, 104, 3, 2)

    ReportService.log("\n=== Перемещения товаров ===")
    try:
        transfer1.execute_transfer()
        ReportService.log(f"Перемещён товар {item1.name} со склада {wh1.name} на {wh2.name}")
    except Exception as e:
        ReportService.log(f"Ошибка перемещения: {e}")

    try:
        transfer2.execute_transfer()
        ReportService.log(f"Перемещён товар {item4.name} со склада {wh3.name} на {wh2.name}")
    except Exception as e:
        ReportService.log(f"Ошибка перемещения: {e}")

    structure = Structure()
    structure.add_warehouse(wh1)
    structure.add_warehouse(wh2)
    structure.add_category(cat1)
    structure.add_category(cat2)
    ReportService.log("\n=== Генерация консольного отчёта ===")
    ReportService.generate_full_report(
        warehouses=[wh1, wh2, wh3],
        sections=[section1, section2],
        categories=[cat1, cat2, cat3],
        suppliers=[supplier1, supplier2],
        transfers=[transfer1, transfer2]
    )

    ReportService.log("=== Сохранение отчётов в JSON и XML ===")
    FileManager.save_to_json(
        "full_report.json",
        warehouses=[wh1, wh2, wh3],
        sections=[section1, section2],
        categories=[cat1, cat2, cat3],
        suppliers=[supplier1, supplier2],
        transfers=[transfer1, transfer2]
    )

    FileManager.save_to_xml(
        "full_report.xml",
        warehouses=[wh1, wh2, wh3],
        sections=[section1, section2],
        categories=[cat1, cat2, cat3],
        suppliers=[supplier1, supplier2],
        transfers=[transfer1, transfer2]
    )

    ReportService.log("Полный отчёт успешно сохранён в full_report.json и full_report.xml")


if __name__ == "__main__":
    main()