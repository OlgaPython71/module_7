class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                file = file.read()
                file = file.lower()
                symbols_to_remove = ',', '.', '=', '!', '?', ';', ':', ' - '
                for symbol in symbols_to_remove:
                    file = file.replace(symbol, "")
                all_words[name] = file.split()
        return all_words

    def find(self, word):
        find_dict = {}
        for name, words in self.get_all_words().items():
            place = words.index(word.lower())+1
            find_dict[name] = place
        return find_dict

    def count(self, word):
        count_dict = {}
        for name, words in self.get_all_words().items():
            quantity = words.count(word.lower())
            count_dict[name] = quantity
        return count_dict



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
