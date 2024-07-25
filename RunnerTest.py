import rt_with_exceptions
import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                        format="%(asctime)s | %(levelname)s | %(message)s", encoding="utf-8")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """Test walk method in runner
        :return
        """
        try:
            rn = rt_with_exceptions.Runner("Micke", -4)
            for i in range(10):
                rn.walk()
            self.assertEqual(rn.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.error(f"Неверная скорость для Runner {err}", exc_info=True)
            # return  -1

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """ Test run method in runner
        :return
        """
        try:
            rn1 = rt_with_exceptions.Runner(25)
            for i in range(10):
                rn1.run()
            self.assertEqual(rn1.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.error(f"Неверный тип данных для объекта Runner {err}", exc_info=True)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """Test of two objects
        :return
        """
        rn2 = rt_with_exceptions.Runner("man")
        rn3 = rt_with_exceptions.Runner("bicycle")
        for i in range(10):
            rn2.walk()
            rn3.run()
        self.assertNotEqual(rn2.distance, rn3.distance)


if __name__ == "__main__":

    unittest.main()




