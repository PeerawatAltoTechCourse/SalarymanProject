#constructor 
class Employee: 
    def __init__(self,engname,engsalary,engmajor): #constructor function syntax
        self.name = engname
        self.salary = engsalary
        self.major = engmajor 
    
    def show(self):
        print("the engineer name :  {}".format(self.name))
        print("and his salary is {}".format(self.salary)) 
        print("graduated {}".format(self.major))


emp1 = Employee("Peerawat",30000,"Power")
emp1.show()
emp2 = Employee("Messi",500000,"Data management")
emp2.show()
# constructor
# [syntax] at 3rd,4th line
# Constructor function will work when there's a creation of an object
# we can set default function of all objects by using constructor
# the constructor always automatic using
# you can create the objects with "the same function" by define the function in "constructor" , 
# so you don't have to define the function everytime you create an object
# See the function of constructor (3rd,4th) work on both created object (15th,17th)