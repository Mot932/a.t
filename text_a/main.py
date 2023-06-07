class TextFile:
    def __init__(self, file="text.txt", mode="r", encoding="UTF-8"):
        self.file = file
        self.mode = mode
        self.encoding = encoding


    def open_file(self):
        with open(self.file, self.mode, encoding=self.encoding) as fileo:
            self.txt = fileo.read()

    def text_read(self):
        self.open_file()
        
    def print_text(self):
        self.text_read()
        print(self.txt)

text_file = TextFile()
text_file.print_text()
