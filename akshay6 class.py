class Employee:
    no_of_leaves = 24
    travelling_passes = 30
    pass




sagar = Employee()
kishor = Employee()


kishor.name = 'kishor'
kishor.salary=15000
kishor.roll = 'maintenace'

sagar.name = 'sagar'
sagar.salary = 15500
sagar.roll = 'jr.engineer'


Employee.no_of_leaves = 10  # you can change vales in calss this way

print(kishor.salary)
print(Employee.no_of_leaves)

