class FileProcess:

    def read_file(path):
        read_file = open(path,"r",encoding="UTF-8")
        print(read_file.read())
        read_file.close()

    def write_file(path,content):
        append_file = open(path,"a",encoding="UTF-8")
        append_file.write(content)
        append_file.close()
if __name__ == '__main__':
    FileProcess.read_file("D:/black/demo.txt")
    FileProcess.write_file("D:/black/demo.txt","\n hello world")