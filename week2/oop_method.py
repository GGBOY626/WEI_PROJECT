class Open:

    def search(self,words, char):
        position = words.find(char)
        if position != -1:
            print(f"char '{char}' in the position: {position}")
        else:
            print(f"char '{char}' not found")

    def print_length(self,words):
        print(f"words length: {len(words)}")

    def print_uppercase(self,words):
        print(f"upper words: {words.upper()}")


if __name__ == "__main__":
    words = input("input words: ")
    char = input("input search char: ")
    name = Open()
    name.search(words,char)
    name.print_length(words)
    name.print_uppercase(words)
