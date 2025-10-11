import unittest
import doctest

def add(x, y):
    """
    Return x + y.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return x + y


def sub(x, y):
    """
    Return x - y.

    >>> sub(5, 3)
    2
    >>> sub(0, 2)
    -2
    """
    return x - y


def div(x, y):
    """
    Return x / y. Raise ZeroDivisionError if y == 0.

    >>> div(6, 3)
    2.0
    >>> div(5, 2)
    2.5
    >>> div(1, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    return x / y


def mod(x, y):
    """
    Return x % y. Raise ZeroDivisionError if y == 0.

    >>> mod(7, 3)
    1
    >>> mod(10, 2)
    0
    >>> mod(5, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: integer modulo by zero
    """
    return x % y


class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 2), -2)

    def test_div(self):
        self.assertEqual(div(6, 3), 2.0)
        self.assertAlmostEqual(div(5, 2), 2.5)
        with self.assertRaises(ZeroDivisionError):
            div(1, 0)

    def test_mod(self):
        self.assertEqual(mod(7, 3), 1)
        self.assertEqual(mod(10, 2), 0)
        with self.assertRaises(ZeroDivisionError):
            mod(5, 0)


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    unittest.main()
