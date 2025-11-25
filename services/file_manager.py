import json
import xml.etree.ElementTree as ET

class FileManager:

    @staticmethod
    def save_to_json(filename, warehouses, sections=None, categories=None, suppliers=None, transfers=None):
        data = {
            "склады": [wh.get_info() for wh in warehouses],
            "секции": [sec.get_info() for sec in sections] if sections else [],
            "категории": [cat.get_info() for cat in categories] if categories else [],
            "поставщики": [sup.get_info() for sup in suppliers] if suppliers else [],
            "перемещения": [tr.get_info() for tr in transfers] if transfers else []
        }
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print("Ошибка при сохранении JSON:", e)

    @staticmethod
    def save_to_xml(filename, warehouses, sections=None, categories=None, suppliers=None, transfers=None):
        root = ET.Element("full_report")

        # Склады
        wh_root = ET.SubElement(root, "warehouses")
        for wh in warehouses:
            wh_elem = ET.SubElement(wh_root, "warehouse", attrib={
                "id": str(wh.warehouse_id),
                "name": wh.name,
                "capacity": str(wh.capacity)
            })
            for item in wh.items:
                ET.SubElement(wh_elem, "item", attrib={
                    "id": str(item.item_id),
                    "name": item.name,
                    "quantity": str(item.quantity),
                    "unit": item.unit,
                    "category": item.category,
                    "expiration_date": getattr(item, "expiration_date", "")
                })

        # Секции
        if sections:
            sec_root = ET.SubElement(root, "sections")
            for sec in sections:
                sec_elem = ET.SubElement(sec_root, "section", attrib={
                    "id": str(sec.section_id),
                    "name": sec.name,
                    "capacity": str(sec.capacity)
                })
                for item in sec.items:
                    ET.SubElement(sec_elem, "item", attrib={
                        "id": str(item.item_id),
                        "name": item.name,
                        "quantity": str(item.quantity),
                        "unit": item.unit,
                        "category": item.category,
                        "expiration_date": getattr(item, "expiration_date", "")
                    })

        # Категории
        if categories:
            cat_root = ET.SubElement(root, "categories")
            for cat in categories:
                ET.SubElement(cat_root, "category", attrib={
                    "id": str(cat.category_id),
                    "name": cat.name
                })

        # Поставщики
        if suppliers:
            sup_root = ET.SubElement(root, "suppliers")
            for sup in suppliers:
                ET.SubElement(sup_root, "supplier", attrib={
                    "id": str(sup.supplier_id),
                    "name": sup.name
                })

        # Перемещения
        if transfers:
            tr_root = ET.SubElement(root, "transfers")
            for tr in transfers:
                ET.SubElement(tr_root, "transfer", attrib={
                    "item_id": str(tr.item_id),
                    "source": str(tr.source_id),
                    "target": str(tr.target_id),
                    "success": str(tr.success)
                })

        tree = ET.ElementTree(root)
        try:
            tree.write(filename, encoding='utf-8', xml_declaration=True)
        except IOError as e:
            print("Ошибка при сохранении XML:", e)
