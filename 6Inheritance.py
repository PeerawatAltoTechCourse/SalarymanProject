class Employee: 
    minSalary = 12000
    maxSalary = 50000
    def __init__(self,engname,engsalary,engmajor): 
        #instanc variable
        self.name = engname
        self.salary = engsalary
        self.major = engmajor 
        
    
    #protected method
    def show(self):
        print("the engineer name :  {}".format(self.name))
        print("and his salary is {}".format(self.salary)) 
        print("graduated {}".format(self.major))


class Accounting(Employee):
    departmentname="accounting"
    def detail(self):
        print("welcome to be an accounting")


acc1=Accounting("Richa",20000)

acc1.detail()
print(acc1.name)
acc1.show()
    
