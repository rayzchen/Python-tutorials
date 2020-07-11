class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    def __str__(self):
        return "My name is " + self.name + " and I am " + str(self.age) + " years old."
        
    def __repr__(self):
        return "'" + self.__str__() + "'"

me = Person("Ray", 12)
print(repr(me))