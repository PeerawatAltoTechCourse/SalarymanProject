#super
class Employee: 
    minSalary = 12000
    maxSalary = 50000
    def __init__(self,engname,engsalary,engdepartment): 
        self.name = engname
        self.salary = engsalary
        self.department = engdepartment 
        
    def show(self):
        print("the engineer name :  {}".format(self.name))
        print("and his salary is {}".format(self.salary)) 
        print("depertment {}".format(self.department))


class Accounting(Employee):
    departmentname="Accounting"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.departmentname)


class Lawer(Employee):
    departmentname="Lawyer"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.departmentname)

class Programmer(Employee):
    departmentname="Programmer"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.departmentname)
    
       

acc1=Accounting("Richa",20000)
acc1.show()

law1=Lawer("Bellingham",40000)
law1.show()

