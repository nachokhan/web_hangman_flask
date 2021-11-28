from unittest import TestCase
from ..app.controller.hangman import get_all_ocurrences

class TestGetAllOcurrences(TestCase):

    def test_1(self):
        letter = 'a'
        word = 'a'
        res = [0]
        self.assertEqual(get_all_ocurrences(word, letter), res, "Error")

    def test_2(self):
        letter = 'a'
        word = 'aa'
        res = [0,1]
        self.assertEqual(get_all_ocurrences(word, letter), res, "Error")

    def test_3(self):
        letter = 'a'
        word = 'aba'
        res = [0, 2]
        self.assertEqual(get_all_ocurrences(word, letter), res, "Error")

    def test_4(self):
        letter = 'a'
        word = 'ba'
        res = [1]
        self.assertEqual(get_all_ocurrences(word, letter), res, "Error")

    def test_5(self):
        letter = 'a'
        word = 'bba'
        res = [2]
        self.assertEqual(get_all_ocurrences(word, letter), res, "Error")

    def test_6(self):
        letter = 'a'
        word = ''
        res = []
        self.assertEqual(get_all_ocurrences(word, letter), res, "Error")

    def test_7(self):
        letter = ''
        word = 'bba'
        res = []
        self.assertEqual(get_all_ocurrences(word, letter), res, "Error")

    def test_8(self):
        letter = 'u'
        word = 'cucurucho'
        res = [1,3,5]
        self.assertEqual(get_all_ocurrences(word, letter), res, "Error")