from BasicWord import BasicWord
from player import Player
from utils import load_random_word

name_user = input('Введите имя игрока: ')
used_words = []
object_player = Player(name_user, used_words)
object_load = load_random_word()
print(f'''Привет {name_user}
Составте {BasicWord.word_count(object_load)} слов из слова {BasicWord.original_word(object_load)}
Слова не должны быть короче 3 букв
Чтобы закончить игру, угадайте все слова или напишите "stop"
Поехали, ваше первое слово?''')
while len(BasicWord.list_admissible_worlds(object_load)) != Player.used_words_count(object_player):
        word_user = input()
        if word_user == 'stop' or word_user == 'стоп':
            break
        if len(word_user) < 3:
            print('Слишком короткое слово')
        if word_user in BasicWord.list_admissible_worlds(object_load):
            if Player.check_use(object_player, word_user):
                print('Слово уже использовано')
            else:
                Player.add_word(object_player, word_user)
                print('Верно')
        else:
            print('Неверное слово')
print(f'Игра завершена, вы угадали {Player.used_words_count(object_player)} слов')