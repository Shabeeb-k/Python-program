# Ooops
"""
class shabeeb:   #class creating
    def IET(self,dep):
        print("studying in dep of\t"+dep)
a=shabeeb()   #object creating
dep="INFROMATION TECHNOLOGY"
a.IET(dep)

"""

"""
class shabeeb():
    def bio(self,n):
        self.name=n
    def biod(self):
        print(self.name)
x=shabeeb()
name="how are you"
y=shabeeb()
y.bio(17)
x.bio(name)
x.biod()
y.biod()

"""
# Constructor
"""
class shabeeb():
    def __init__(self,name,age,dep,year):   #this is a constructor
        self.name=name
        self.age=age
        self.dep=dep
        self.year=year


x=shabeeb("shabeeb",17,"IT","fourth year")
"""

"""

class Employee:
    year=2001
    def __init__(self, name, id,age,dep,place):
        self.id = id
        self.name = name
        self.age=age
        self.dep=dep
        self.place=place

    def add_age(self):
        self.age=self.age+1

    def relocate_dep(self,dep):
        self.dep=dep

    def display(self):
        print("name is :"+self.name)
        print("id is :%d" %self.id)
        print("year is :" + str(Employee.year))
        print("age is :" + str(self.age))
        print("dep is :"+self.dep)
        print("place is :" + self.place)



emp1 = Employee("John", 101,20,"Informarion technology","tvm")
emp2 = Employee("David", 102,40,"electronics","ekm")


Employee.year=Employee.year+1

emp2.add_age()
emp1.add_age()


emp1.display()
print("_____________")
emp2.display()
"""
"""

#object instance variables(self.)
class Employee:
    year = 2012

    def __init__(self, name, id, age, dep, place):
        self.id = id
        self.name = name
        self.age = age
        self.dep = dep
        self.place = place

    def add_age(self,):
        self.age = self.age + 1

    def relocate_dep(self, dep):
        self.dep = dep

    def display(self):
        print("name is :" + self.name)
        print("id is :%d" % self.id)
        print("year is :" + str(Employee.year))
        print("age is :" + str(self.age))
        print("dep is :" + self.dep)
        print("place is :" + self.place)

    @classmethod  # used for only class variable and it contain a function also
    def add_year(cls):
        cls.year = cls.year + 1

    @staticmethod
    def main_display():
        print("EMPLOYEE DETAILS IS:")

emp1 = Employee("John", 101, 20, "Informarion technology", "tvm")
emp2 = Employee("David", 102, 40, "electronics", "ekm")

Employee.main_display()
emp1.display()
print("_____________")
emp2.display()
print("_____________")
Employee.add_year()  # class name vechitt aaa fn call cheythu
emp1.add_age()
emp1.relocate_dep("civil engineering")#changing the departmnet

emp1.display()
print("_____________")
emp2.add_age()
emp2.relocate_dep("printing technology")#changing the department
emp2.display()
"""