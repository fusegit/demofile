#maltileval inheritance
class Employee:
    empname='raju'
    pay=2451365
    def emp(self):
     print(f'empmname {self.empname},PAY {self.pay}')

    def __init__(self) -> None:
        print('in superclass con')
class Manegar(Employee):
    mname='jon'
    sal=1245135
    add='us'
    def man(self):
     print(f'mname {self.mname},SAL {self.sal} ADD{self.add}')

    def __init__(self) -> None:
        print('insub class con')
class Md(Manegar):
    mdname="Ankush"
    share='100%'
    add ='claliforniya'
    def md(self):
       print(f'MDNAME{self.mdname}, SHARE {self.share}, Add{self.add}')

    def __init__(self) -> None:
        print('sub class con')


md=Md()
md.md()
md.man()
md.emp()
man=Manegar()
man.man()
man.emp()
