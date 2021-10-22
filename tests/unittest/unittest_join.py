import unittest
from testable.join import join


class TestSum(unittest.TestCase):

    def test_join_int(self):
        self.assertEqual(join(1, 2, 3), '1234')

    def test_join_str(self):
        self.assertEqual(join('1', '2', '3'), '123')

    def test_join_mixed(self):
        self.assertEqual(join(1, '2', [3]), '12[3]')


if __name__ == '__main__':
    unittest.main()
