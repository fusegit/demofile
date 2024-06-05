avalue= 'welcome'
print(avalue)

print(len(avalue))

##endwith

isend=avalue.endswith('come')

print(isend)############ttrue

isend=avalue.endswith('wel')
print(isend) ######## false

isend=avalue.endswith('e')
print(isend) ######## true

################################################
#33333   count function


scount=avalue.count('e')
print(scount)################## 2

scount=avalue.count('wel')
print(scount)############## 1


################# find function

afind=avalue.find('e')
print(afind)         #########   1

afind=avalue.find('come')
print(afind)         #########   3

######### find the 2 number substring

sfind='e'
ssfind=avalue.find(sfind)
print(ssfind)

srplace=avalue.capitalize()
print(srplace)

srplace=avalue.replace('come','done')
print(srplace)