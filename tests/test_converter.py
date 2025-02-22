import unittest
from main import text_to_morse


class TestTextToMorse(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(text_to_morse('SOS'), '... --- ...')
        self.assertEqual(text_to_morse('HELLO'), '.... . .-.. .-.. ---')


if __name__ == '__main__':
    unittest.main()
