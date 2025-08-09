class Open:
    def __init__(self, words):
        self.words = words

    def search(self, char):
        position = self.words.find(char)
        if position != -1:
            print(f"char '{char}' in the position: {position}")
        else:
            print(f"char '{char}' not found")

    def print_length(self):
        print(f"words length: {len(self.words)}")

    def print_uppercase(self):
        print(f"upper words: {self.words.upper()}")


if __name__ == "__main__":
    words = input("input words: ")
    char = input("input search char: ")

    obj = Open(words)
    obj.search(char)
    obj.print_length()
    obj.print_uppercase()
