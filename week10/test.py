"""test example"""
class Test:

    def __init__(self, data):
        """"init"""
        self.data = data

    def get_length(self):
        """get length"""
        return len(self.data)

    def count_uppercase(self):
        if isinstance(self.data, str):
            return sum(1 for char in self.data if char.isupper())
        if isinstance(self.data, list):
            return sum(
                1 for item in self.data if isinstance(item, str)
                for char in item if char.isupper()
            )
        return 0


if __name__ == "__main__":

    analyzer1 = Test("Hello World!")
    print("Length:", analyzer1.get_length())
    print("Uppercase letters:", analyzer1.count_uppercase())

    analyzer2 = Test(["Python", "AI", "Test"])
    print("Length:", analyzer2.get_length())
    print("Uppercase letters:", analyzer2.count_uppercase())
