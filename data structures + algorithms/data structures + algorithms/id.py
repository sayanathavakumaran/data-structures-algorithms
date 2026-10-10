class Person():
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self,age):
        self.age = age

    def get_country(self):
        return self.country

    def set_country(self,country):
        self.country = country

person1 = Person("person1","15","uk")
person2 = Person("person2","21","usa")
person1.set_name("sayana")
print(person1.get_name())
person1.set_age("22")
print(person1.get_age())
person1.set_country("switzerland")
print(person1.get_country())