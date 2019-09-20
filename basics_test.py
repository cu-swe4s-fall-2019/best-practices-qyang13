import unittest
import random
import statistics as stats
import get_column_stats as gcs


class TestColumnStats(unittest.TestCase):
    def test_calcMean_const(self):
        testVec = list(range(500))
        self.assertEqual(gcs.calcMean(testVec), stats.mean(testVec))

    def test_calcMean_random(self):
        testVec = random.sample(range(1, 100), 10)
        self.assertEqual(gcs.calcMean(testVec), stats.mean(testVec))

    def test_calcMean_invalidInput(self):
        self.assertRaises(TypeError, gcs.calcMean, None)
        self.assertRaises(TypeError, gcs.calcMean, 'Foo')
        self.assertRaises(TypeError, gcs.calcMean, 1)

    def test_calcStdev_const(self):
        testVec = list(range(500))
        self.assertAlmostEqual(gcs.calcStdev(testVec),
                               stats.stdev(testVec), places=0)

    def test_calcStdev_random(self):
        testVec = random.sample(range(1, 500), 100)
        self.assertAlmostEqual(gcs.calcStdev(testVec),
                               stats.stdev(testVec), places=-1)

    def test_calcStdev_invalidInput(self):
        self.assertRaises(TypeError, gcs.calcStdev, None)
        self.assertRaises(TypeError, gcs.calcStdev, 'Foo')
        self.assertRaises(TypeError, gcs.calcStdev, 1)


if __name__ == '__main__':
    unittest.main()
