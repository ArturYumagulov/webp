from PIL import Image
import os

from settings import *
from ready.reader import excel_reader
path = "C:\\Users\\YumagulovA\\Pictures"


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


def path_remove(path):
    result = []
    for path, dirs, files in os.walk(path):
        for file in files:
            if file[-3:] == "jpg":
                # print(f"{path}\\{file}")
                # result.append(f"{path}\\{file}")
                result.append([path, file])

            elif file[-3:] == 'png':
                # print(f"{path}\\{file}")
                # result.append(f"{path}\\{file}")
                result.append([path, file])

            elif file[-3:] == 'svg':
                # print(f"{path}\\{file}")
                # result.append(f"{path}\\{file}")
                result.append([path, file])

            elif file[-3:] == 'JPG':
                # print(f"{path}\\{file}")
                # result.append(f"{path}\\{file}")
                result.append([path, file])

            elif file[-4:] == 'jpeg':
                # print(f"{path}\\{file}")
                # result.append(f"{path}\\{file}")
                result.append([path, file])

    return result


if __name__ == '__main__':
    # for i in excel_reader(IMAGE_PATH, SHEET_NAME):
    data = path_remove(path)
    for i in data:
        print(i[0] + i[1])
        conv_to_webp(i[0], i[1])
        break
    #     try:
    #         conv_to_webp(f'/Users/arturumagulov/Yandex.Disk.localized/Загрузки/wwwroot{i}', i)
    #         print("save")
    #     except FileNotFoundError:
    #         print("Not Found")
    # print(path_remove(path))



