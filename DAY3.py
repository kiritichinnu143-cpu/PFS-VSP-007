''''
DATA TYPES --> IT WILL TELL US HOW TO DEFINE DATA
NUMERIC DATATYPES --> INTEGER,FLOAT,COMPLEX
BOOLEAN VALUES-->TRUE/FALSE
NONE TYPE -->NONE
SEQUENCE TYPES --> STRING,LISTD,SETS,FROZENSETS,MAPPINGS(DICTIONARIES)

#NUMERIC DATATYPES ->INTRGER -->QUANTITIES,IDS,ORDER IDS,STOCK,AGE-->INT
age=32
print(age)
print(type(age))
stock=35
print(type(stock))
batch_rank=12
print(type(batch_rank))


#float values--> salaries,price,percentage calculations,temp.....
salary=45000.56
print(salary)
print(type(salary))
temp=34.5
print(type(temp))

#complex-->real and imaginary values -->scientific calcus,signal processing
i5=23
data=3+i5
print(data)

data=3+5j
print(data)
print(type(data))


#boolean -->true/false -->validations
access=True
print(access)
print(type(access))

access=False
print(access)
print(type(access))


#none type -->None -->>0,false,"",'',{},(),[],set() are none cases in python
rank=None
print(type(rank))

#TYPE CONVERSION ->CONVERTING ONE DATATYPE TO ANOTHER DATATYPE
#EXPLICT CONVERSION
#INTEGER -->FLOAT,COMPLEX,BOOLEAN
#EVERY BUILT-IN DATATYPES IS A BUILT-IN FUNCTION
rank=5
print(type(rank))
b=float(rank)
print(b)
print(type(b))
c=complex(rank)
print(c)
d=bool(rank)
print(d)
print(type(d))
a=bool( )
print(a)
print(type(a))
#space is also a character
print(bool(' '))

#float--> integer,complex,boolean
b=88.8
print(complex(b,5))
print(int(b))
print(bool(b))

#complex-->int,float,bool

signal=5+6j

print(float(signal))
#print(int(signal))
print(bool(signal))

#bool-->int,float,complex
access=True
print(int(access))
print(complex(access))
print(float(access))

a=(int(float(bool(5))))
print(a)
b=bool(float(int(34)))
print(b)

c=True+35+3.5+(4+5j)
print(type(c))
print(c)

#sequence types --> string,list,sets,frozensets,dictionaries
#string-->quotations--> single,double,triple quotes
#string are immutuable,ordered,indexed collection 
a='saketh'
print(type(a))
print(a)
b="sak"
a=b
print(a)
print(len(a))#len(obj)-->returns the number of items in a collection
#space also as a character
marks=True
print(str(marks))
print(str(marks))
'''
