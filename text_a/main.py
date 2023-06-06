class TextFile:
    def __init__(self, file="text.txt", mode="r", encoding="UTF-8"):
        self.file = file
        self.mode = mode
        self.encoding = encoding

    def open_file(self):
        with open(self.file, self.mode, encoding=self.encoding) as file_object:
            return file_object.read()

    def text_read(self):
        text = self.open_file()
        return text

    def print_text(self):
        text = self.text_read()
        print(text)


TextFile().print_text()
