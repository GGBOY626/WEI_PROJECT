class Teacher:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print('teacher name is '+self.name)
class Student(Teacher):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        print(f'student name is {self.name}')

if __name__ == '__main__':
    t = Teacher('mike')
    s = Student('tom')
    t.speak()
    s.speak()
