class TextAnalyser:
    def __init__(self, file_name=None):
        """ вызывает цепочку методов """
        if file_name is None:
            raise Exception("Не указан файл для анализа!")
        self.read_file(file_name)
        self.prepare_text()
        self.print_text()

    def read_file(self, file_name):
        """ пытается открыть файл и считать его в строку """
        try:
            with open(file_name, "r", encoding="UTF-8") as file:
                self.file = file  # здесь получается файловый объект
                self.text = self.file.read()  # здесь получается строка текста
        except FileNotFoundError:
            raise Exception(f"Файл {file_name} не найден!")

        if not self.text.strip():
            raise Exception("Прочитанный файл пуст!")

    def prepare_text(self):
        """приводит текст к нижнему регистру"""
        self.text = self.text.lower()        

    def print_text(self):
        """ выводит строку текста на экран """
        print(self.text)


TextAnalyser(file_name="text.txt")
