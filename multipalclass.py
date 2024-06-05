
class Employee:
    empid = 101
    name = "Shubham"
    address = "Pune"
    salary = 3000000

    def getInfo(self):
        print(f"Info : empId : {self.empid}, Name : {self.name}, address :{self.address}" )

    def updateInfo(self, empid : int, name :str, address : str) -> str: 
        self.empid = empid
        self.name = name            # emp.name = "Nikhil"
        self.address = address

emp = Employee()
emp.getInfo()       #Info : empId : 101, Name : Shubham, address :Pune

emp.updateInfo(2002, "Nikhil", "Mumbai")
emp.getInfo()  


##============================================================================

class Student:
    studid = 101
    name = "Shubham"
    address = "Pune"

    def getInfo(self):
        print(f"Info : studId : {self.studid}, Name : {self.name}, address :{self.address}" )

    def updateInfo(self, studid : int, name :str, address : str) -> str: 
        self.studid = studid
        self.name = name            # emp.name = "Nikhil"
        self.address = address

stud = Student()
stud.getInfo()       #Info : studId : 101, Name : Shubham, address :Pune

stud.updateInfo(2002, "Nikhil", "Mumbai")
stud.getInfo()  


# # # len()
# # # index(alist)
# # # index(adictionary)

# # # class str:
# # #     def index():


# # # class list:
# # #     def index():

