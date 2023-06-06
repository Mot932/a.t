class TextFile:
    def __init__(self, txt):
        self.txt = txt

    
    def read(self):
        self.file = open(self.txt, "r", encoding="UTF-8")
        text = self.file.read()
        return text
    
    def print_content(self):
        text = self.read()
        print(text)

fileO = TextFile("text.txt")
fileO.print_content()