class Employee:
    no_of_leaves = 24
    travelling_psses =30
    def __init__(self,rname,rsalary,rrole,): # how to use constructor
        self.name = rname #self means kishor or sagar
        self.salary = rsalary
        self.role = rrole

    def printdetails(self):
        return f"the name is {self.name} and salary is {self.salary} AND role is {self.role} and his traveling passes are {Employee.travelling_psses}"


    @classmethod                        #classmethod is only use for change perticular class vales like read line number 20
    def change_leave(cls,new_leaves):
        cls.no_of_leaves= new_leaves

    @classmethod                      #this classmethod is only for to avoid writing this kishor = Employee('Kishor',15000,'maintainance engineer')
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
      return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)  #hay kay tari use


kishor = Employee('Kishor',15000,'maintainance engineer')
sagar  = Employee('Sagar',15500,'jr.engineer')
akshay = Employee .from_dash("Akshay-45000-coder")


sagar.change_leave(10)
# print(sagar.no_of_leaves)
# print(sagar.printdetails())
print(akshay.salary)