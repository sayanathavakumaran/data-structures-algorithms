class Person():
    def __init__(self,name,age,contact):
        self.name = name
        self.age = age
        self.contact = contact
        print("inside person init")
    def show_details(self):
        print(self.name)
        print(self.age)
        print(self.contact)
class Employee(Person):
    def __init__(self,name,age,contact,salary,manager,department):
        Person.__init__(self,name,age,contact)
        self.__employeeid = 0
        self.salary = salary
        self.manager = manager
        self.department = department
        print("inside employee init")
    def show_details(self):
            print(self.name)
            print(self.age)
            print(self.contact)
            print(self.salary)
            print(self.manager)
            print(self.department)
    def change_id(self,newid):
         self.__employeeid = newid 
employee = Employee("name1","age1","contact1","salary1","manager1","department1")
employee.show_details()
employee.__employeeid = 6
employee.change_id(7)
print(employee.__employeeid)
print(employee._Employee__employeeid)