class Question:
    def __init__(self, text_question: str, complexity: int, right_answer: str):
        self.text_question = text_question
        self.complexity = complexity
        self.right_answer = right_answer
        self.question_asked = False
        self.question_answer = None
        self.points = int(self.complexity) * 10

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.points

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.right_answer.lower() == self.question_answer.lower()

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'Вопрос: {self.text_question}\nСложность {self.complexity}/5'


    def build_positive_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        return f'Ответ верный, получено {self.points} баллов'


    def build_negative_feedback(self):
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        return f'Ответ неверный, верный ответ {self.right_answer}'

