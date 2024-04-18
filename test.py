import unittest
from career import main


class TestMainFunction(unittest.TestCase):

    def test1(self):
        lines = ["4\n", "4\n", "3 1\n", "2 1 5\n", "1 3 2 1\n"]
        main()
        with open("career.out", "r") as file:
            content = file.read().strip()
            self.assertEqual(int(content), 15)

    def test2(self):
        lines = ["3\n", "3\n", "3 4\n", "7 6 9\n"]
        main()
        with open("career.out", "r") as file:
            content = file.read().strip()
            self.assertEqual(int(content), 15)


if __name__ == '__main__':
    unittest.main()
