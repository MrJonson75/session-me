# # -*- coding: utf-8 -*-
import unittest
import runner_and_tournament

'''
#       Цель: освоить методы, которые содержит класс TestCase.
#
#         Задача:
#       В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub.
#     (Можно скопировать)
#       В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и
#     новый класс Tournament.
#
#         Изменения в классе Runner:
#
#        Появился атрибут speed для определения скорости бегуна.
#     Метод __eq__ для сравнивания имён бегунов.
#     Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
#       Класс Tournament представляет собой класс соревнований, где есть дистанция, которую
#     нужно пробежать и список участников. Также присутствует метод start, который реализует
#     логику бега по предложенной дистанции.
#
#   Напишите класс TournamentTest, наследованный от TestCase. 
#   В нём реализуйте следующие методы:
#
# setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут
# сохраняться результаты всех тестов.
#
# setUp - метод, где создаются 3 объекта:
# Бегун по имени Усэйн, со скоростью 10.
# Бегун по имени Андрей, со скоростью 9.
# Бегун по имени Ник, со скоростью 3.
# tearDownClass - метод, где выводятся all_results по очереди в столбец.
#
# Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
# У объекта класса Tournament запускается метод start, который возвращает словарь в
# переменную results. В конце вызывается метод assertTrue, в котором сравниваются
# последний объект из result и предполагаемое имя последнего бегуна (индекс -1).
# Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект
# Tournament соблюсти):
#
# Усэйн и Ник
# Андрей и Ник
# Усэйн, Андрей и Ник.
#
# Как можно понять:
#
# Ник всегда должен быть последним.
#
# Дополнительно (не обязательно, не влияет на зачёт):
# В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка.
# В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции
# быстрее, чем бегун с большей.
# Попробуйте решить эту проблему и обложить дополнительными тестами.
# Пример результата выполнения тестов:
# Вывод на консоль:
# {1: Усэйн, 2: Ник}
# {1: Андрей, 2: Ник}
# {1: Андрей, 2: Усэйн, 3: Ник}
#
# Ran 3 tests in 0.001s
# OK
#
# Примечания:
# Ваш код может отличаться от строгой последовательности описанной в задании.
# Главное - схожая логика работы тестов и наличие всех перечисленных переопределённых
# методов из класса TestCase.
'''


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""

        print("===================================")
        out ={}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                out[k] = str(v)
            print(value)

    def setUp(self):
        """Set up for test"""
        self.usain = runner_and_tournament.Runner("Усэйн", 10)
        self.andrew = runner_and_tournament.Runner("Андрей", 9)
        self.nick = runner_and_tournament.Runner("Ник", 3)
        print("Set up for [" + self.shortDescription() + "]")

    def test_start_tour_1(self):
        """first run / первый забег"""
        print("id: " + self.id())
        tour = runner_and_tournament.Tournament(90, self.usain, self.nick)
        results = tour.start()
        last_runner = list(results.values())
        self.assertTrue(last_runner[-1] == "Ник")
        self.all_results[self.shortDescription()] = results

    def test_start_tour_2(self):
        """second run / второй забег"""
        print("id: " + self.id())
        tour = runner_and_tournament.Tournament(90, self.andrew, self.nick)
        results = tour.start()
        last_runner = list(results.values())
        self.assertTrue(last_runner[-1] == "Ник")
        self.all_results[self.shortDescription()] = results

    def test_start_tour_3(self):
        """third run / третий забег"""
        print("id: " + self.id())
        tour = runner_and_tournament.Tournament(90, self.andrew, self.usain, self.nick)
        results = tour.start()
        last_runner = list(results.values())
        self.assertTrue(last_runner[-1] == "Ник")
        self.all_results[self.shortDescription()] = results


if __name__ == "__main__":
    unittest.main()
