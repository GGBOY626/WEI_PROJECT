from typing import List


class LibraryItem:
    def __init__(self,title,author):
        self.__title = title
        self.__author = author

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    def display(self):
        return f'title is {self.title}, author is {self.author}'

class Book(LibraryItem):
    def __init__(self,title,author):
        super().__init__(title,author)
    def display(self):
        return f'the book of title is {self.title}, the book of author is {self.author}'
class Magazine(LibraryItem):
    def __init__(self,title, author,issue_frequency):
        super().__init__(title, author)
        self.issue_frequency = issue_frequency

    def display(self):
        return f'the magazine of title is {self.title}, the magazine of author is {self.author}, the magazine of issue_frequency is {self.issue_frequency}'
class Library:
    def __init__(self):
        self._items: List[LibraryItem] = []

    def add_item(self, item: LibraryItem):
        self._items.append(item)

    def remove_item(self, title: str):
        for i, it in enumerate(self._items):
            if it.title == title:
                self._items.pop(i)
                return True
        return False

    def update_item(self, title: str, new_item):

        for i, it in enumerate(self._items):
            if it.title == title:
                self._items[i] = new_item
                return True
        return False

    def display_all(self):
        if not self._items:
            return "[Library] No items."
        return "\n".join(it.display() for it in self._items)

if __name__ == "__main__":
    lib = Library()
    lib.add_item(Book("Clean Code", "Robert C. Martin"))
    lib.add_item(Magazine("ACM Communications", "ACM Editors", "Monthly"))
    print(lib.display_all())
    lib.update_item("Clean Code", Book("Refactoring", "Martin Fowler"))
    print(lib.display_all())
    lib.remove_item("ACM Communications")
    print(lib.display_all())