# name='rohit'
# id=101
# def info():
#     print(f'name:{name}\n id:{id}')

# info()


# def info():
#     print('hello')

# info()

# def mono():
    # pass

####################################################################3

def info(inputstring):
    print(inputstring.upper())
info('hell')

#########################################3
#########function with return type statement

# def rfun(sendstring:str):
#     return 'hello'+sendstring
#     print('after return')   #333333333333 not executed after resurn
    
# result=rfun('jaddo')

# print(result)
############################################

def getInUpper(inputStr : str = 'world'):       # providing parameter type is optional
    if (inputStr == 'credence'):
        return "Hello " + inputStr.upper() 
    else:
         return "Invalid input"
    
##1
result = getInUpper("credence")        #Hello CREDENCE
print(result)

# # ##1
result = getInUpper("pune")        #invalid input
print(result)
