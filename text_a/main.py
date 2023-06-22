class TextAnalyser:
    def __init__(self, file_name=None) -> None:
        """ вызывает цепочку методов """
        if file_name is None:
            raise Exception("Не указан файл для анализа!")
        self.file_name = file_name
        self.read_file()
        self.check_empty_file()
        self.prepare_text()
        self.print_text()

    def read_file(self) -> None | NoReturn:
        """ пытается открыть файл и считать его в строку """
        try:
            with open(self.file_name, "r", encoding="UTF-8") as file:
                self.file = file
                self.text = self.file.read()
        except FileNotFoundError:
            raise Exception(f"Файл {self.file_name} не найден!")

    def check_empty_file(self) -> None | NoReturn:
        if not self.text:
            raise RuntimeError(f"Прочитанный файл: {self.file_name}, пуст!")

    def prepare_text(self) -> None:
        """приводит текст к нижнему регистру"""
        self.text = self.text.lower()
        for char in punctuation.replace("-", "—"):
            self.text = self.text.replace(char, "")
        self.words = self.text.split()
    
    def print_text(self) -> None:
        """ выводит строку текста на экран """
        print(self.words)
        print(f"В этом тексте {len(self.words)} слов")


TextAnalyser(file_name="text.txt")
