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
