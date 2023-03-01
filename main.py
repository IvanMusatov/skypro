import json
import random
from question import Question

with open('questions.json', 'r', encoding='utf-8') as file:
    '''Чтение файла, подготовка для создания списка'''
    text = json.load(file)


def list_question():
    '''Создание списка объектов'''
    question_list = []
    question_list_random = []
    for part in text:
        question_list.append(Question(part["q"], part["d"], part["a"]))
        question_list_random = random.sample(question_list, len(question_list))
    return question_list_random


def result():
    '''Результат работы программы'''
    answers_count = 0
    points_count = 0
    print('Игра начинается!')
    for item in list_question():
        print(f'Вопрос {Question.build_question(item)}')
        answers_count += 1
        user_answer = input()
        item.question_answer = user_answer
        if Question.is_correct(item):
            points_count += Question.get_points(item)
            print(Question.build_positive_feedback(item))
        else:
            print(Question.build_negative_feedback(item))
    print(f'Вот и всё!\nОтвечено {answer_count} вопроса из {len(list_question())}\nНабрано балло: {points_count}')


if __name__ == "__main__":
    result()

print('HelloWorld')