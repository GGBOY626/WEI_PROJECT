class FileProcess:
    def __init__(self, path):
        self.path = path
    def read_file(self):
        read_file = open(self.path,"r",encoding="UTF-8")
        print(read_file.read())
        read_file.close()

    def write_file(self,content):
        append_file = open(self.path,"a",encoding="UTF-8")
        append_file.write(content)
        append_file.close()
if __name__ == '__main__':
    fp = FileProcess("D:/black/demo.txt")
    fp.read_file()
    fp.write_file("\n hello world")