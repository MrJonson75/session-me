import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """Test walk method in runner
        :return
        """
        rn = runner.Runner("child")
        for i in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """ Test run method in runner
        :return
        """
        rn1 = runner.Runner("Auto")
        for i in range(10):
            rn1.run()
        self.assertEqual(rn1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """Test of two objects
        :return
        """
        rn2 = runner.Runner("man")
        rn3 = runner.Runner("bicycle")
        for i in range(10):
            rn2.walk()
            rn3.run()
        self.assertNotEqual(rn2.distance, rn3.distance)


if __name__ == "__main__":
    unittest.main()
