#######print 1 to 20 number
# for item in range(1,11):
#     print(item)
# print('after for lopp')

###############################################

# ilist=[1,2,3,4,5,'ram']

# for con in ilist:
#     print(con)
#     print(ilist)
# #     ##############################

# ilist=[1,2,3,4,5,'ram']

# for con in ilist:
#    # print(con)
#     print(ilist)

# #####################################    

# alist=[1,2,3,4,5,6,'ram','shyam','radha']

# ab=6

# for temp in range(ab,9):
#     print(alist[temp])

# print( 'after loop')

# #######################################3

# iList = [10, 30, 90, 20, 60]
# for temp in range(-3,1):
#      print(f"Value at index {temp} is {iList[temp]}")



# iList = [10, 30, 90, 20, 60]
# for temp in range(0, 5, 2):
#      print(f"Value at index {temp} is {iList[temp]}")


# ############# continue
# ####want a evan numbeer
# ilist=[10,31,90,267,61]
# for temp in ilist:
#     if temp % 2 ==0:
#         continue
#     print(temp)
# print('class leval')    


# ####print number in list is even and oddd......

alist=[10,2,6,5,1,4,2,7,9,6,8,85,17,45,21,36,24,51]

for temp in alist:
    if temp % 2==0:
        print(f'{temp} is evan number')
    else:
        print(f'{temp} is a odd number')

print(len(alist))