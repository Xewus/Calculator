import sys
import unittest
from pathlib import Path

import deck

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(BASE_DIR / "deck")


class TestDeck(unittest.TestCase):
    """Тестирование последовательности `deck.Deck`.
    """
    @classmethod
    def setUpClass(cls):
        cls.test_deck = deck.Deck(5)
        cls.error_func_msg = "Некорректное работа функции: "

    def setUp(self):
        TestDeck.test_deck_2 = deck.Deck(5)
        TestDeck.test_deck_3 = deck.Deck(9)
        TestDeck.test_deck_3.push_back(1)
        TestDeck.test_deck_3.push_back(9)

    def test_str_repr(self):
        repr_deck = "Deck: size=5, fullness=0"
        str_deck = "[None, ..., None]"
        self.assertEqual(
            repr(TestDeck.test_deck), repr_deck,
            f"{TestDeck.error_func_msg}`__repr__()`"
        )
        self.assertEqual(
            str(TestDeck.test_deck), str_deck,
            f"{TestDeck.error_func_msg}`__str__()`"
        )

    def test_len(self):
        self.assertEqual(
            len(TestDeck.test_deck), 0,
            f"{TestDeck.error_func_msg}`__len__()`"
        )

    def test_eq(self):
        error_msg = f"{TestDeck.error_func_msg}`__eq__()`"
        self.assertTrue(
            TestDeck.test_deck == TestDeck.test_deck_2,
            error_msg
        )
        self.assertTrue(
            TestDeck.test_deck != TestDeck.test_deck_3,
            error_msg
        )
        self.assertFalse(
            TestDeck.test_deck != TestDeck.test_deck_2,
            error_msg
        )
        self.assertFalse(
            TestDeck.test_deck == TestDeck.test_deck_3,
            error_msg
        )

        TestDeck.test_deck_2.push_back(1)
        self.assertTrue(
            TestDeck.test_deck != TestDeck.test_deck_2,
            error_msg
        )
        self.assertFalse(
            TestDeck.test_deck == TestDeck.test_deck_2,
            error_msg
        )

    def test_lt(self):
        error_msg = f"{TestDeck.error_func_msg}`__lt__()`"
        self.assertFalse(
            TestDeck.test_deck > TestDeck.test_deck_2,
            error_msg
        )
        self.assertFalse(
            TestDeck.test_deck < TestDeck.test_deck_2,
            error_msg
        )
        self.assertTrue(
            TestDeck.test_deck <= TestDeck.test_deck_2,
            error_msg
        )
        self.assertTrue(
            TestDeck.test_deck >= TestDeck.test_deck_2,
            error_msg
        )
        self.assertTrue(
            TestDeck.test_deck < TestDeck.test_deck_3,
            error_msg
        )
        self.assertTrue(
            TestDeck.test_deck_3 >= TestDeck.test_deck_2,
            error_msg
        )

        TestDeck.test_deck_2.push_back(1)
        self.assertTrue(
            TestDeck.test_deck < TestDeck.test_deck_2,
            error_msg
        )
        self.assertTrue(
            TestDeck.test_deck <= TestDeck.test_deck_2,
            error_msg
        )
        self.assertFalse(
            TestDeck.test_deck > TestDeck.test_deck_2,
            error_msg
        )
        self.assertFalse(
            TestDeck.test_deck >= TestDeck.test_deck_2,
            error_msg
        )

    def test_size(self):
        error_msg = f"{TestDeck.error_func_msg}`size()`"
        self.assertEqual(
            TestDeck.test_deck_2.size(), 5, error_msg
        )
        self.assertEqual(
            TestDeck.test_deck_3.size(), 9, error_msg
        )

    def test_clear(self):
        error_msg = f"{TestDeck.error_func_msg}`clear()"
        TestDeck.test_deck_2.push_back(9)
        TestDeck.test_deck_2.push_front(1)
        self_id = id(TestDeck.test_deck_2)
        self.assertEqual(
            str(TestDeck.test_deck_2), "[1, ..., 9]"
        )
        TestDeck.test_deck_2.clear()
        self.assertEqual(
            str(TestDeck.test_deck_2), "[None, ..., None]",
            error_msg
        )
        self.assertEqual(
            id(TestDeck.test_deck_2), self_id,
            error_msg
        )

    def test_push_back(self):
        error_msg = f"{TestDeck.error_func_msg}`push_back()"
        self_len = len(TestDeck.test_deck_2)
        self_size = TestDeck.test_deck_2.size()
        TestDeck.test_deck_2.push_back(1)
        self.assertCountEqual(
            str(TestDeck.test_deck_2), "[1, ..., 1]",
            error_msg
        )
        self.assertEqual(
            len(TestDeck.test_deck_2), self_len + 1,
            error_msg
        )
        TestDeck.test_deck_2.push_back(9)
        self.assertCountEqual(
            str(TestDeck.test_deck_2), "[1, ..., 9]",
            error_msg
        )
        self.assertEqual(
            len(TestDeck.test_deck_2), self_len + 2,
            error_msg
        )
        self.assertEqual(
            TestDeck.test_deck_2.size(), self_size,
            error_msg
        )

    def test_push_front(self):
        error_msg = f"{TestDeck.error_func_msg}`push_front()"
        self_len = len(TestDeck.test_deck_2)
        self_size = TestDeck.test_deck_2.size()
        TestDeck.test_deck_2.push_front(8)
        self.assertCountEqual(
            str(TestDeck.test_deck_2), "[8, ..., 8]",
            error_msg
        )
        self.assertEqual(
            len(TestDeck.test_deck_2), self_len + 1,
            error_msg
        )
        TestDeck.test_deck_2.push_front(2)
        self.assertCountEqual(
            str(TestDeck.test_deck_2), "[2, ..., 8]",
            error_msg
        )
        self.assertEqual(
            len(TestDeck.test_deck_2), self_len + 2,
            error_msg
        )
        self.assertEqual(
            TestDeck.test_deck_2.size(), self_size,
            error_msg
        )

    def test_pop_back(self):
        error_msg = f"{TestDeck.error_func_msg}`pop_back()"
        self_size = TestDeck.test_deck_3.size()
        self_len = len(TestDeck.test_deck_3)
        value = TestDeck.test_deck_3.pop_back()
        self.assertEqual(
            len(TestDeck.test_deck_3), self_len - 1,
            error_msg
        )
        self.assertEqual(
            value, 9,
            error_msg
        )
        self.assertCountEqual(
            str(TestDeck.test_deck_3), "[1, ..., 1]",
            error_msg
        )
        self.assertEqual(
            TestDeck.test_deck_3.size(), self_size,
            error_msg
        )

    def test_pop_front(self):
        error_msg = f"{TestDeck.error_func_msg}`pop_front()"
        self_size = TestDeck.test_deck_3.size()
        self_len = len(TestDeck.test_deck_3)
        value = TestDeck.test_deck_3.pop_front()
        self.assertEqual(
            len(TestDeck.test_deck_3), self_len - 1,
            error_msg
        )
        self.assertEqual(
            value, 1,
            error_msg
        )
        self.assertCountEqual(
            str(TestDeck.test_deck_3), "[9, ..., 9]",
            error_msg
        )
        self.assertEqual(
            TestDeck.test_deck_3.size(), self_size,
            error_msg
        )

    def test_get_back(self):
        error_msg = f"{TestDeck.error_func_msg}`get_back()"
        self_size = TestDeck.test_deck_3.size()
        self_len = len(TestDeck.test_deck_3)
        value = TestDeck.test_deck_3.get_back()
        self.assertEqual(
            len(TestDeck.test_deck_3), self_len,
            error_msg
        )
        self.assertEqual(
            value, 9,
            error_msg
        )
        self.assertCountEqual(
            str(TestDeck.test_deck_3), "[1, ..., 9]",
            error_msg
        )
        self.assertEqual(
            TestDeck.test_deck_3.size(), self_size,
            error_msg
        )

    def test_get_front(self):
        error_msg = f"{TestDeck.error_func_msg}`get_front()"
        self_size = TestDeck.test_deck_3.size()
        self_len = len(TestDeck.test_deck_3)
        value = TestDeck.test_deck_3.get_front()
        self.assertEqual(
            len(TestDeck.test_deck_3), self_len,
            error_msg
        )
        self.assertEqual(
            value, 1,
            error_msg
        )
        self.assertCountEqual(
            str(TestDeck.test_deck_3), "[1, ..., 9]",
            error_msg
        )
        self.assertEqual(
            TestDeck.test_deck_3.size(), self_size,
            error_msg
        )


if __name__ == '__main__':
    unittest.main()
