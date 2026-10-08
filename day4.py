'''
list--> A list is an ordered,mutable,indexed and heterogenous collection
were we use [] to reprsent lists
student details,order details,stock entries...

details=[1,'saketh','pfs7','vizag',56.7]
print(len(details))
print(type(details))

stu_ids=['cgv1','cgv2','cgv3']
#print(stu_ids[1])
stu_ids[0]='code'#here we are using indexing
print(stu_ids[0])
print(stu_ids)

#tuple-->A tuple are also immutable,ordered,indexed and heterogenous
#collections,we use() parenthis
#dimensions,coordinates

place=('vizag','hyd','vzm')
print(type(place))
print(place)
print(place[0])

dimensions=10,20,30# by default it become tuple
print(dimensions)
print(type(dimensions))
l,b,h=10,20,30
print(l,b,h)
print(type(l))

#sets-->A set is unique collection(removes duplicates) which doesn't allow duplicates
#A set is unordered,unindexed,mutuable collection
ids=set()#empty set
print(ids)
ids=set([123,134,145,156])
print(ids)
print(type(ids))
a=set((1,2,3,4))
print(a)
print(type(a))
course={'pf','da','jfs'}
print(course)

#Dictonaries-->A dictonary (mapping object) is a collection of
#key value pairs -->dict=={k:v},we acces only by keys(indexed by keys)
#dictonaries is also mutable collection
details={'branch':'vskp',
         'batches':['pfs-007','pfs-004','pfs-005'],
         'course':'pfs',
         'count':19}
print(len(details))
print(details['course'])# we can only access by giving only keys
print(len(details['batches']))

#every built-in datatypes is a built-in function
#int,float,complex,bool,str,list,tuple,set,dict
#lists-->tuples,set,dict,str
a=[1,2,3]
print(tuple(a))
print(set(a))
print(str(a))
print(dict(a))

a=set((1,2,3))
print(type(a))
print(tuple(a))
print(str(a))
print(list(a))

print(dict.fromkeys(a))

#frozensets-->it is an immutable
a=frozenset((12,34,54,34))
print(list(a))
print(tuple(a))
print(set(a))
print(dict.fromkeys(a))
print(len(dict.fromkeys(a)))
a='dad'
print(list(a))
print(tuple(a))
print(set(a))
print(dict.fromkeys(a))
print(len(dict.fromkeys())
#Operators --> Arithematic Operators,Assignment,Comparision.
#Logical,Membership,Identity,Bitwise Operators

#Arthmetic Operators --> +,-,*,/(float division), // (floor Division) Quotient
# % Modulus(remainder), **(Exponential)
a=3
a=2
b=3
print(a*b)
print(a+b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
'''







