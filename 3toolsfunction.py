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
emp2 = Employee("Messi",500000,"Data management")

print(emp1.__class__)

# class
# check the class of the object  
