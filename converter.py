from PIL import Image
import os

from settings import *
from ready.reader import excel_reader


class ImageConv:

    def __init__(self, path):
        self.path = path

    def walker(self):
        for i in os.walk(self.path):
            print(i)
            return i[2]

    def conv_to_webp(self, lst):
        for name in lst:
            im = Image.open(f"{self.path}/{name}").convert("RGB")
            im.save(f"ready\\{name[:-3]}webp", "webp")

    def conv_to_ico(self, lst):
        for name in lst:
            im = Image.open(f"{self.path}\\{name}").convert("RGB")
            im.save(f"ready\\{name[:-3]}ico", "ico")


def conv_to_webp(path, name):
    clear_name = name.replace('/', '_')
    # print(clear_name)
    im = Image.open(path).convert("RGB")
    im.save(f"read/{clear_name[:-3]}webp", "webp")


if __name__ == '__main__':
    for i in excel_reader(IMAGE_PATH, SHEET_NAME):
        try:
            conv_to_webp(f'/Users/arturumagulov/Yandex.Disk.localized/Загрузки/wwwroot{i}', i)
            print("save")
        except FileNotFoundError:
            print("Not Found")


