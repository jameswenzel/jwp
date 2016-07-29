import unittest
from utils import *
from jwp.jwmultithreaded import *


class multithreadedTest(unittest.TestCase):

    def test_multithread(self):
        results = multithread(test, [[1, 2, 3], [4, 5, 6]])
        self.assertTrue(results)
        results = multithread(test, [[1, 2, 3], [4, 5, 6]], chunksize=2, maxtasksperchild=2)
        self.assertTrue(results)

    def test_safe_multithread(self):
        results = safe_multithread(test, [[1, 2, 3], [4, 5, 6]])
        self.assertTrue(results)
        results = safe_multithread(test, [[1, 2, 3], [4, 5, 6]], chunksize=2)
        self.assertTrue(results)

    def test_multithread_failsafe(self):
        results = multithread_failsafe(test, [[1, 2, 3], [4, 5, 0]])
        self.assertTrue(results)
        self.assertTrue(len(results) == 1)
        results = multithread_failsafe(test, [[1, 2, 3], [4, 5, 0]], chunksize=2)
        self.assertTrue(results)
        self.assertTrue(len(results) == 1)

    def test_safe_multithread_failsafe(self):
        results = safe_multithread_failsafe(test, [[1, 2, 3], [4, 5, 0]])
        self.assertTrue(results)
        self.assertTrue(len(results) == 1)
        results = safe_multithread_failsafe(test, [[1, 2, 3], [4, 5, 0]], chunksize=2)
        self.assertTrue(results)
        self.assertTrue(len(results) == 1)

if __name__ == '__main__':
    unittest.main()