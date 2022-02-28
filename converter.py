from PIL import Image
import os


class ImageConv:

    def __init__(self, path):
        self.path = path

    def walker(self):
        for i in os.walk(self.path):
            return i[2]

    def conv_to_webp(self, lst):
        for name in lst:
            im = Image.open(f"{self.path}\\{name}").convert("RGB")
            im.save(f"ready\\{name[:-3]}webp", "webp")

    def conv_to_ico(self, lst):
        for name in lst:
            im = Image.open(f"{self.path}\\{name}").convert("RGB")
            im.save(f"ready\\{name[:-3]}ico", "ico")


# if __name__ == '__main__':
#     # t = ImageConv('image')
#     # t.conv_to_webp(t.walker())
