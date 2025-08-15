class CountWords:
    def __init__(self, path):
        self.path = path

    def count_words(self):
        read_file = open(self.path, "r", encoding="UTF-8")
        text = read_file.read()
        result = len(text.split())
        read_file.close()
        return result
if __name__ == '__main__':
    fp = CountWords("D:/black/demo.txt")
    print(fp.count_words())