class Analizat_Text:
    def __init__(self, file="text.txt", mode="r", encoding="UTF-8"):
        self.file = file
        self.mode = mode
        self.encoding = encoding
        self.text_read()
        self.print_text()

    def open_file(self):
        with open(self.file, self.mode, encoding=self.encoding) as file_object:
            return file_object.read()

    def text_read(self):
        self.txt = self.open_file()

    def print_text(self):
        print(self.txt)


test_file = Analizat_Text()
