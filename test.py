import unittest

import separator
from some_modules import functions_for_testing as fft
from some_modules import classes_for_testing as cft


# Тестирование функций
class NamesTestCase(unittest.TestCase):
    """ Тестируем name_function """

    # Наименование функций тестирования лучше начинать со слова test_,
    # тогда тестирование будет запускаться автоматом при запуске файла с тестами
    def test_first_last_name(self):
        """ Проверка на Андрей Хаккерных """
        formatted_name = fft.get_formatted_name('андрей', 'хаккерных')

        self.assertEqual(formatted_name, 'Андрей Хаккерных')

    def test_first_last_middle_name(self):
        """ Проверка Андрей Великолепнович Хаккерных """
        formatted_name = fft.get_formatted_name('андрей', 'хаккерных', 'хаккерных')

        self.assertEqual(formatted_name, 'Андрей Хаккерных Хаккерных')


separator.print_separator()


# Тестирование классов
class AnonymousSurveyTestCase(unittest.TestCase):
    def test_store_single_response(self):
        """ Проверка сохранения одного ответа """
        question = 'Ты в порядке?'
        answer = 'Заебца!'

        survey = cft.AnonymousSurvey(question)
        survey.store_response(answer)

        self.assertIn(answer, survey.responses)

    def test_store_tree_answers(self):
        question = 'Ты в порядке?'
        answers = ['Заебца!', 'Чётко!', 'Ништяк!']

        survey = cft.AnonymousSurvey(question)

        for answer in answers:
            survey.store_response(answer)

        for answer in answers:
            self.assertIn(answer, survey.responses)


# Преднастройка объектов для тестирования
class AnonymousSurveySetupTestCase(unittest.TestCase):
    def setUp(self):
        """ Подготовка вопросов и ответов """
        question = 'Ты в порядке?'

        self.survey = cft.AnonymousSurvey(question)

    def test_store_single_response(self):
        """ Проверка сохранения одного ответа """
        answer = 'Заебца!'

        self.survey.store_response(answer)

        self.assertIn(answer, self.survey.responses)

    def test_store_tree_answers(self):
        answers = ['Заебца!', 'Чётко!', 'Ништяк!']

        for answer in answers:
            self.survey.store_response(answer)

        for answer in answers:
            self.assertIn(answer, self.survey.responses)


if __name__ == '__main__':
    unittest.main()
