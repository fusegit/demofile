class Billcust:
    id=1001
    name='janu'
    bill=00

    def __init__(self) :
     print("in first con")

    def __init__(self):
      print("in consture")
      self.id=102
      self.name='ramu'
      self.bill=1236
    def getdata(self):
       return f"ID:{self.id},NAME:{self.name} BILL:{self.bill}"

bill=Billcust()
bill1=Billcust()
bill.getdata()
print(bill.getdata())
# ##########################################
# class Con:
#     def __init__(self) -> None:
#         print('in 1 con')

#     def __init__(self) -> None:
#         print('in 2 con')
# c=Con()
# c=Con()

# # c.__init__()
# # print(c)
# # print(c)