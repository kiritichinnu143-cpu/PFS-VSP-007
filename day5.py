'''
#operators--> operators help us to perform operational between operands

Arithmetric operator-->+,-,*,%(remainder),//(integer or floor division),/

Assignment Operators --> it help us to assign ,update(increment),decrement values

#=(assigning),+=(addtion&assign),-=(subtraction&assign),
# *=(multiplication&assign) /=,//=,**=,%=


data=20
print(data)
print(type(data))

stock=data
print(stock)

#increment
stock=stock+5
print(stock)

#decrement
data-=2
print(data)
print(data-2)
r=1,2,3
print(r[1]-1)
print(r[1]*2)
print(r[1]/2)
print(r[1]//2)


#comparision operator (relational operator)--> it performs comparsion
#between the operands and result in boolean true/false-->conditions
#==,!=,<,<=,>,>=
name='kalyani'
k_attendance=80
print(k_attendance==75)
print(k_attendance<=75)
print(k_attendance>=75)
print(k_attendance<75)
print(k_attendance>75)
print(k_attendance!=75)


#logical operator-->and,or,not(keywords)and gives us boolean values
#and--> it need all condition must be true or satisfy the condition
#or-->it need any one condition to be satisfied
#not-->opp to exisiting

max_marks =80
v_mar=76
max_att=75
v_att=70

certificate=v_mar>=max_marks and v_att>=max_att
print(certificate)
v_mar+=5
certificate=v_mar>=max_marks or v_att>=max_att
print(certificate)

data=[]
print(data)
print(not(data))
data=[1,2,3]
print(not(data))

#membership operators--> in,not in,

names=['vijay','vinay','raju','balakrishna']
name=['ajay']
print(name in names)
print(names in  name)
print(name not in names)

print(['ajay'] not in ['ajay'])

#identify operators--> it specifically refers to the object (memory locatio)
#id --> is ,is not
a=15
b=14
print(a==b)
print(id(a))
print(id(b))
c=a
print(id(c))

a=(1,2,3,4)
b=(1,2,3,4)
print(id(a))
print(id(b))
a=[1,2,3,4]
b=[1,2,3,4]
print(id(a))
print(id(b))

a=set([1,2,3,4])
b=set([1,2,3,4])
print(id(a))
print(id(b))

a={}
b={}
print(id(a))
print(id(a))

a=(1,2,3,4)
b=(1,2,3,4)
print(id(a))
print(id(b))
print(a is b)
# when we check with the interpreter mode and scripting mode above
#tuple result changes

#Bitwise operator--> it performs bitwise operations -->&(bitwise and)
#|(bitwise or),^(bitwise xor)
#An integer will be converted binary format and performs bitwise operation
#following integer to binary conversion
print(7&3)
print(7|3)
print(7^3)
print(5^2)
#shifting opeartor(<<,>>)
print(7<<1)
print(5>>1)
'''



















