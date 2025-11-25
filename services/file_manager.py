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
