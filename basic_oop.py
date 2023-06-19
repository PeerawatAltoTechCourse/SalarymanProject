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



#[syntax] def detail(self,name,salary) , we add parameters to () of the function
# the name and salary means you need to put them on to have successful using the function
# 5th,6th lines means attribute is a parameter we define in finction() 
# the attribute parameters name must be the same as parameter we put in the funtion() 
# and already define in the function() that authorized  the attributes 
# 12th-15th we put parameter info into the object that working by the function
# we can have employee info more than one 





