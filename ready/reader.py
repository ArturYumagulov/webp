import openpyxl as xl
from settings import IMAGE_PATH, SHEET_NAME


def excel_reader(file_obj: str, sheet_name: str) -> list:
    """Функция чтения файла для передачи в модуль инициализации БД"""

    result = []
    wb = xl.load_workbook(file_obj)
    sheet = wb[sheet_name]
    for i in sheet:
        for ii in i:
            result.append(ii.value)
    return result


if __name__ == '__main__':
    print(excel_reader(IMAGE_PATH, SHEET_NAME))
