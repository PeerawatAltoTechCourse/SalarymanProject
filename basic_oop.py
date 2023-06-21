#project salary man
#intruct how to work
class Employee: #class created
    def detail(self,engname,engsalary,engmajor):
        self.name = engname
        self.salary = engsalary
        self.major = engmajor 
        print("the engineer name :  {}".format(self.name))
        print("and his salary is {}".format(self.salary)) 
        print("graduated {}".format(self.major))

#object created
#working
emp1 = Employee()
emp1.detail("Peerawat",30000,"Power")

emp2 = Employee()
emp2.detail("Messi",500000,"Data management")








