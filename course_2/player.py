class Player:
    def __init__(self, name, used_words = []):
        '''Содержит имя пользователя и использованные слова'''
        self.name = name
        self.used_words = used_words

    def __repr__(self):
        return f'{self.name} {self.used_words}'

    def used_words_count(self) -> int:
        '''Получение количества использованных слов'''
        return len(self.used_words)

    def add_word(self, word_user):
        '''Добавление слова в использованные слова'''
        self.used_words.append(word_user)

    def check_use(self, word_user) -> bool:
        '''Проверка использовалось ли слово ранее'''
        use_check = word_user in self.used_words
        return use_check

