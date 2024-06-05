aset={1,2,22,33,22,1,2,3,4,5,6,55,11,22,11,6}

print(len(aset))
print(aset)
aset.update((10,20,30))
print(aset)

print(aset.pop())
print(aset.pop())
print(aset.pop())
print(aset.pop())

bset={1,2,3,3,4,5,4,5,2,3}
cset={1,2,4,5,6,3,8,9,1,2}
print(bset.union(cset))
print(bset.intersection(cset).pop())

print(bset.remove(3))
print(bset)
cset.remove(2)
print(cset)