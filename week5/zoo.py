# Parent class: Color
class Color:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Color: {self.name}"


# Child class: TransparentColor (inherits from Color)
class TransparentColor(Color):
    def __init__(self, name: str, alpha: float):
        super().__init__(name)
        self.alpha = alpha       # transparency (0 ~ 1)

    def __str__(self):
        return f"TransparentColor: {self.name}, alpha={self.alpha}"


# Animal class
class Animal:
    def __init__(self, species: str, color: Color):
        self.species = species
        self.color = color

    def __str__(self):
        return f"Animal: {self.species}, {self.color}"


# Demo
if __name__ == "__main__":
    lion = Animal("Lion", Color("Yellow"))
    jellyfish = Animal("Jellyfish", TransparentColor("White", 0.3))

    print(lion)
    print(jellyfish)
