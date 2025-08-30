class Teacher:
    def __init__(self,name,visa_card,bank_account):
        self.name = name
        self._visa_card = visa_card
        self.__bank_account = bank_account
    def speak(self):
        print('teacher _visa_card is '+self._visa_card)

    def speak2(self):
        print('teacher bank_account is ' + self.__bank_account)
class Student:
    def __init__(self, name, visa_card, bank_account):
        self.name = name
        self._visa_card = visa_card
        self.__bank_account = bank_account
    def show(self):
        # public
        print("Student can access public name:", self.name)
        # protect
        print("Student can access protected visa_card:", self._visa_card)
if __name__ == '__main__':
    t = Teacher("Mike", "VISA-123", "BANK-456")
    t.speak()
    t.speak2()
    s = Student("Tom", "VISA-789", "BANK-999")
    s.show()

