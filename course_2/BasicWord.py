class BasicWord:
    def __init__(self, word : str, admissible_words : list):
        '''Содержит исходное слово и набор допустимых подслов'''
        self.word = word
        self.admissible_words = admissible_words

    def __repr__(self):
        return f'{self.word} {self.admissible_words}'

    def original_word(self):
        '''Возвращает исходное слово'''
        return self.word

    def check(self) -> bool:
        '''Проверка введенного слова в списке допустимых подслов'''
        word_check = word_user in self.admissible_words
        return word_check

    def word_count(self) -> int:
        '''Возвращает исходное слово'''
        return len(self.admissible_words)

    def list_admissible_worlds(self):
        '''Возвращает список правильных слов'''
        return self.admissible_words
