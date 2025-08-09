class Open:
    def search(words):

        print(len(words))
        result = words.upper()
        print(result)


if __name__ == "__main__":
    print("please input the words")
    words = input()
    Open.search(words)