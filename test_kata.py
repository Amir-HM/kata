import unittest
import kata

class TestConv(unittest.TestCase):

    def test_conv(self):
        self.assertEqual(kata.c_f(20), 68, "The answer should be 68")


if __name__ == '__main__':
            unittest.main()
