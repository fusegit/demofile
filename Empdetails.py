class Empdetails:
    id=101
    name='motu'
    com='tech mahindra'

    def getinfo(self):
         print('in methord')
         print(f'ID:{self.id}\n NAME:{self.name}\n COM:{self.com}')    
    def update(self,uid,uname,ucom):
         print('in update')
         self.id=uid
         self.name=uname
         self.com=ucom

#Empdetails.getinfo()
#getinfo()
emp=Empdetails()
emp.getinfo()
emp.update(102,"raj",'hexa')
emp.getinfo()