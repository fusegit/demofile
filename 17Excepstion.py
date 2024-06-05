# a=[1,2,3,4,5]

# try:
#     print(a[0])
#     print(a[1])
#     print(a[5])
#     print(a[3])

# except:
#     print('givan iindex is not available in list')
#     print('in except')
#    # print(a[5])

# print(a[4])

# ###########################################################################

try:
    num=int(input('enter a number divisiabl by 100'))
    result=100/num
    print(result)

except Exception as e:
    print('the excepction is :', e)

# ################################################################################

# try:    
#     inputNumber = input("Enter number to divide to 100 : ")
#     try:
#         result = 100 / int(inputNumber)
#         print("Result : ", result)
#     except:
#         print("Can not perform division operation")

# except ZeroDivisionError as z:
#     print("YOu can not enter 0 as input")
# except Exception as ex:
#     print("Error Occured : ", ex)

# finally:
#     print('in finnaly')