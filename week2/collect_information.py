class Collect:
    def __init__(self, list):
        self.list = list
    def collect(self,name,age,address):
        information = [name,age,address]
        return information
    def update_age(self,information,add_age):
        information[1] = int(int(information[1])+int(add_age))
        return information


if __name__ == "__main__":
    name = input("input your name: ")
    age = input("input your age: ")
    address = input("input your address: ")
    list = [name,age, address]
    obj = Collect(list)
    information=obj.collect(name,age,address)
    print("your basic information:",information)
    add_age = input("update your age: ")
    result = obj.update_age(information,add_age)
    print("update your age:",result)