"""test example"""
from typing import Iterable, List, Union


TextLike = Union[str, List[str]]
class Test:

    def __init__(self, data):
        """"init"""
        self.data = data

    def _iter_chars(self) -> Iterable[str]:
        """Yield characters from self.data, flattening lists if needed."""
        if isinstance(self.data, str):
            yield from self.data
        elif isinstance(self.data, list):
            for item in self.data:
                if isinstance(item, str):
                    yield from item

    def get_length(self):
        """get length"""
        return len(self.data)

    def count_uppercase(self):
        if isinstance(self.data, str):
            return sum(1 for char in self.data if char.isupper())
        if isinstance(self.data, list):
            return sum(
                1 for item in self.data if isinstance(item, str)
                for char in item if char.isupper()
            )
        return 0
        # ---------- new APIs for Activity 2 ----------

    def count_digits(self) -> int:
        """count digit characters 0–9"""
        return sum(1 for ch in self._iter_chars() if ch.isdigit())

    def count_specials(self, ignore_space: bool = True) -> int:
        """
        count special characters (non-alphanumeric).
        By default, spaces/tabs/newlines are NOT counted. Set ignore_space=False to include them.
        """

        def is_special(ch: str) -> bool:
            if ignore_space and ch.isspace():
                return False
            return not ch.isalnum()

        return sum(1 for ch in self._iter_chars() if is_special(ch))


if __name__ == "__main__":
    analyzer1 = Test("Hello World! #2025")
    print("Length:", analyzer1.get_length())
    print("Uppercase letters:", analyzer1.count_uppercase())
    print("Digits:", analyzer1.count_digits())
    print("Specials (no spaces):", analyzer1.count_specials())

    analyzer2 = Test(["Python3", "AI-101", "Test!"])
    print("Length:", analyzer2.get_length())
    print("Uppercase letters:", analyzer2.count_uppercase())
    print("Digits:", analyzer2.count_digits())
    print("Specials (no spaces):", analyzer2.count_specials())
