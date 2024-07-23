# # -*- coding: utf-8 -*-
import unittest
import runner_and_tournament




class TournamentTest(unittest.TestCase):
    is_frozen = True

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
            print(out)

    def setUp(self):
        """Set up for test"""
        self.usain = runner_and_tournament.Runner("Усэйн", 10)
        self.andrew = runner_and_tournament.Runner("Андрей", 9)
        self.nick = runner_and_tournament.Runner("Ник", 3)
        print("Set up for [" + self.shortDescription() + "]")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_tour_1(self):
        """first run / первый забег"""
        print("id: " + self.id())
        tour = runner_and_tournament.Tournament(90, self.usain, self.nick)
        results = tour.start()
        last_runner = list(results.values())
        self.assertTrue(last_runner[-1] == "Ник")
        self.all_results[self.shortDescription()] = results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_tour_2(self):
        """second run / второй забег"""
        print("id: " + self.id())
        tour = runner_and_tournament.Tournament(90, self.andrew, self.nick)
        results = tour.start()
        last_runner = list(results.values())
        self.assertTrue(last_runner[-1] == "Ник")
        self.all_results[self.shortDescription()] = results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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
