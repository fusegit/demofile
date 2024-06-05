adist={ 101:'pratik',
        'institude':'crediance',
        True:"ram",
        'per':100 ,   
        '102':'raju'

}

print(adist)
print(type(adist))
print(len(adist))

print(adist[True])
print(adist['institude'])
print(adist.items())
print(adist.keys())
print(adist.get('per'))
adist['institude']='nit'
print(adist['institude'])

adist.update({'per':100,'cgpa':85})
print(adist['cgpa'])

print(adist.get('102'))
print(adist.values)

adist.update({'pyare':'mohan',1002:1245})

print(adist)