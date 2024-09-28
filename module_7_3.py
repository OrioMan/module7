import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()  # Прочитать содержимое файла в нижнем регистре
                text = text.translate(str.maketrans('', '', string.punctuation))  # Удалить пунктуацию
                words = text.split()  # Разбить текст на слова
                all_words[file_name] = words  # Записать в словарь

        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word.lower() in words:
                position = words.index(word.lower())  # Найти первое вхождение
                result[file_name] = position + 1  # Добавить 1 для удобства
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count = words.count(word.lower())  # Подсчитать вхождения
            if count > 0:
                result[file_name] = count
        return result

# Пример использования:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
