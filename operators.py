# operators in python
# arithmetic operators
from operator import truediv

a=5
b=4
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a/b)

x=3
x=x+3
print(x)
y=3
y+=3
print(y)

# comparison operators
# >tham
age1=23
age2=45
age3=age1>age2
print(age3)
# the output will be false otherwise will b true,it is a boolean op
# <than
age4=56
age5=23
age6=age4<age5
print(age6)

# marks
# >=
marks1=200
marks2=300
marks3= marks1>=marks2
print(marks3)

# <=
marks4=242
marks5=147
marks6=marks4<=marks5
print(marks6)

# one equals sign assigns a value
# two equals signs checks if the values are equal
# ==
marks7=15
marks8=8
print(marks7==marks8)

# !=
marks9=65
marks10=91
print(marks9!=marks10)


# declare four variables and calculate the summation of each pair then do a comparison
a=20
b=30
c=40
d=50
e=a+b
print(e)
f=c+d
print(f)

g=e<f
print(g)

h=e>f
print(h)

i=e<=f
print(i)

k=e>=f
print(k)

l=e==f
print(l)

m=e!=f
print(m)


# logical operators
# FT=False
# TF=False
# FF=False
# TT=True



student1=23
student2=67
student3=45
student4=35
# and
print(student1>student2 and student3>student4)
print(student1<student2 and student3<student4)
print(student1>student2 and student3<student4)
print(student1<student2 and student3>student4)

# or
# so long as one is true,the output is true
print(student1>student2 or student3>student4)
print(student1>student2 or student3<student4)
print(student1>student2 or student3<student4)
print(student1<student2 or student3>student4)


# not
print(not(student1<student2 or student3>student4))


# take  4 students age  as input and perform logical operations with the keyed in values
a1=int(input('Enter your age : '))
a2=int(input('Enter your age : '))
a3=int(input('Enter your age : '))
a4=int(input('Enter your age : '))
print(a1,a2,a3,a4)
print(a1>a2 and a3>a4)
print(a1>a2 or a3>a4)
print(not(a1<a2 or a3>a4))
















