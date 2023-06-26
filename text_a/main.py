import re
import pymorphy3
from typing import NoReturn

class TextAnalyser:
    def __init__(self, file_name=None) -> None:
        """
        Инициализирует объект TextAnalyser.
        Параметры:
        - file_name (строка, по умолчанию None): Имя файла для анализа.
        Возвращает: None.
        Выбрасывает исключение Exception, если не указан file_name.
        Вызывает методы read_file(), check_empty_file(), prepare_text(), gwbp() и print_text().
        """
        if file_name is None:
            raise Exception("Не указан файл для анализа!")
        self.file_name = file_name
        self.read_file()
        self.check_empty_file()
        self.prepare_text()
        self.gwbp()
        self.print_text()

    def read_file(self) -> None | NoReturn:
        """
        Читает содержимое указанного файла и сохраняет текст.
        Возвращает: None | NoReturn.
        Может вызывать исключение FileNotFoundError, если файл не найден.
        """
        try:
            with open(self.file_name, "r", encoding="UTF-8") as file:
                self.file = file
                self.text = self.file.read()
        except FileNotFoundError:
            raise Exception(f"Файл {self.file_name} не найден!")

    def check_empty_file(self) -> None | NoReturn:
        """
        Проверяет, является ли прочитанный текст пустым.
        Возвращает: None | NoReturn.
        Может вызывать исключение RuntimeError, если текст пуст.
        """
        if not self.text:
            raise RuntimeError(f"Прочитанный файл: {self.file_name}, пуст!")

    def prepare_text(self) -> None:
        """
        Предварительно обрабатывает текст, приводя его к нижнему регистру и удаляя небуквенно-цифровые символы, 
        кроме пробелов и дефисов. Разделяет текст на отдельные слова.
        Возвращает: None.
        """
        self.text = self.text.lower()
        clean_text = ''.join(re.findall(r'[\w\s-]', self.text))
        self.words = clean_text.split()

    def gwbp(self, pos_list=["VERB", "NOUN"]) -> None:
        """
        Фильтрует слова по заданным частям речи с использованием библиотеки pymorphy3.
        Параметры:
        - pos_list (список строк, по умолчанию ["VERB", "NOUN"]): Список желаемых частей речи.
        Возвращает: None.
        """
        morph = pymorphy3.MorphAnalyzer()
        self.words_by_pos = []

        for word in self.words:
            parsed_word = morph.parse(word)
            found_word = False
            for parse in parsed_word:
                if any(pos in parse.tag for pos in pos_list):
                    self.words_by_pos.append(parse.normal_form)
                    break

    def print_text(self) -> None:
        """
        Выводит исходные слова, общее количество слов и отфильтрованные слова.
        Возвращает: None.
        """
        print(self.words)
        print(f"Отфильтрованные слова: {self.words_by_pos}")
        print(f"В этом тексте {len(self.words)} слов")
        print(f"В этом тексте {len(self.words_by_pos)} отфильтрованных слов")
        

TextAnalyser(file_name="text.txt")
