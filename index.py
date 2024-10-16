

print("Martin Njue")
print("Welcome to class")
print(345)
print("345")
print(100.5)
# variables
name="Martin Njue"
print(name)
age=17
print(age)
marks=78.4
print(marks)
a=5
b="school"
print(a)
print(b)

# Data types
# integer
d=45
print(d)
print(3543)


# string
g="please come  here"
print(g)
print("Please knock first")


# boolean

is_boy=True
print(is_boy)
is_girl=False
print(is_girl)


# float
l=23.54
print(l)
print(43.342)

# Input from user
last_name=input("What is your last name? ")
print(last_name)
age=input("How old are you?")
print(age)
height=input("How tall are you?")
print("You are " + height + " inches tall.")
weight=input("How much do you weigh?")
print("You are " + weight)
family_name=input("What is your family name? ")
print("Good Morning " + family_name)


f_name=input("What is your first name? ")

l_name=input("What is your last name? ")

profession=input("What is your profession? ")

print("Hello " + f_name + " "+ l_name + " you are a " + profession)

# Type Conversion
first_number= int(input("Enter first number: "))
print(first_number)
second_number=int(input("Enter second number: "))
print(second_number)
sum=first_number+second_number
print("The sum is " + str(sum))

sub=first_number-second_number
print("The difference is" + str(sub))


y=float(input("Enter first mark: "))
x=float(input("Enter second mark: "))
minus=y - x
print("The difference is " + str(minus))

# take in a persons height and weight and calculate the BMI of the individual then display the BMI to the person

name=input("What is your name? ")
height=float(input("How tall are you in inches? "))
weight=float(input("How much do you weigh in kilograms ?"))
bmi=weight/(height*height)
print("Welcome " + str(name) + "You are " + str(height) + "inches tall" + "and "+ str(weight) + "kilograms" )
print("Your BMI is " + str(bmi) + "kg/m2")
print("Thank You")
