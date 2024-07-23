import unittest
import RunnerTest
import TournamentTest

my_suite = unittest.TestSuite()
my_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.RunnerTest))
my_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(my_suite)