class Teacher:
# ----------------- Explanation -----------------
# public attribute like name can use by anywhere
# protect attribute like _visa_card suggested by subclass
# private only use by internal class like __bank_account only use in Teacher
    def __init__(self,name,visa_card,bank_account):
        self.name = name # public
        self._visa_card = visa_card #protect
        self.__bank_account = bank_account #private
    def speak(self):
        print('teacher _visa_card is '+self._visa_card)

    def speak2(self):
        print('teacher bank_account is ' + self.__bank_account)
class Student(Teacher):
    def __init__(self, name, visa_card, bank_account):
        super().__init__(name, visa_card, bank_account)
    def show(self):
        # public
        print("Student can access public name:", self.name)
        # protect
        print("Student can access protected visa_card:", self._visa_card)
        # private
        # print(self.__bank_account)  # subclass can not use private attribute
if __name__ == '__main__':
    t = Teacher("Mike", "VISA-123", "BANK-456")
    t.speak()
    t.speak2()
    s = Student("Tom", "VISA-789", "BANK-999")
    s.show()

