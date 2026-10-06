'''
#name,email,mobile,gender='simmu','simmu@gmail.com',657473673674,'male'
#print(name)
#name='sim';mobile=111
#del name,mobile
#print(mobile,name)
a,b =15,25
print(a)
print(b)
a,b=b,a
print(a)
print(b)

c=a# ressigning the existing value to a new variable
print(c)

#literals--> these are constants such as numbers(int,float,complex)
age=33.5
print(age)
print(type(age))
price=44
print(type(price))

#identifiers--> names given to variables,object,class,functions,modules

#punctuators-->{}-->lists,()-->tuples,[]-->dictonaries,sets
#operators-->there are different type of operators--> operations
#+,-,*,**,/(arithmetric operators),//,%
a=5
b=3
print(a/b)#/--> float division (answer is always in float value)
print(a//b)#//--> flooring division(integer division) returns quotient
print(a%b)#%-->modulus returns remainder
'''
price=1000
discount=0.15
final_price=price-(price*discount)
print(final_price)


bill=2500
gst=0.5
discount=0.5
total_price=bill+(bill*gst)
print(total_price)
last_price=total_price-(total_price*discount)
print(last_price)
