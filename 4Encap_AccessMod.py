#Access Modify
class Employee: 
    def __init__(self,engname,engsalary,engmajor): 
        #protected attribute
        self._name = engname
        self._salary = engsalary
        self._major = engmajor 
    
    #protected method
    def _show(self):
        print("the engineer name :  {}".format(self._name))
        print("and his salary is {}".format(self._salary)) 
        print("graduated {}".format(self._major))

    

emp1 = Employee("Peerawat",30000,"Power")
emp2 = Employee("Messi",500000,"Data management")


