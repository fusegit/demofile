###singal heritance
class Employee:
    name='parth'
    add='nagour'
    mono=124563
   
    def __init__(self) -> None:
        print('in super con')
         
    def getinfo(self):
        print(f'name {self.name} add {self.add} mono {self.mono}')

class Temp(Employee):
    name='ank'
    add='pue'
    sal=500000

    def __init__(self) -> None:
        print('in chiled con')

    def gettemp(self):
        print( f'name {self.name}, add {self.add}, mono {self.sal}')


sub=Employee()
sub.getinfo()
tsub=Temp()
tsub.gettemp()
tsub.getinfo()