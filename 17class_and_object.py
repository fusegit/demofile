# name='kl rahul'
# id=101
# add='lkn'

# def getinfo():
#     print(f'NAME:{name} ID:{id} ADD:{add}')

# getinfo()

# print('inside class')
# ###########################################
class Employee:
    name='ms dhoni'
    id=107
    add='chennai'
    print('hello class')
    print(name)
    def getcomname(self):
     print('cred')

    def empinfo(self):
        print(f'NAME:{self.name} ID:{self.id} ADD:{self.add}')

   # getcomname()

#Employee.getcomname()
    
print('out of class')
print(Employee.name)

emp=Employee()
#Employee.getcomname()
emp.getcomname()
Employee.empinfo(emp)
emp.empinfo()
emp.getcomname()
print(emp.name)
# #############
Employee.getcomname(emp)