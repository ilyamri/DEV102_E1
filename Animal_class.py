class Animal:
    """
    Animal class with name and age.
    """

    def __init__(self, name="n", age=0):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

if __name__ == "__main__":
    a = Animal("Cat", 3)
    print(a.get_name())
    print(a.get_age())
