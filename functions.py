def my_function():
    print("Hello,welcome to functions")
    print("Hello,welcome to functions")
    print("Hello,welcome to functions")


my_function()
my_function()
my_function()


def my_string():
    hello = "Good morning,welcome back"
    print(hello)

my_string()


def my_var(name):
    print(name)


my_var('George')
my_var('Peter')
my_var('John')


# function with one argument
def my_conc(firstname):
    print('Hello '+firstname+'Please enter ')


my_conc('Esther')
my_conc('Vivian')
my_conc('Boaz')
my_conc('Derrick')

# function with two arguments
def two(name,age):
    print('Hello ' + name + ' you are '+ str(age) + ' years old')


# type 'the name between single quotes' and then a comma and then the age,it will autocomplete

two('Pauline',40)
two('Jane',26)
two('Evans',34)

# function with three arguments/parameters
def welcome(firstname,lastname,age):
    print('Hello '+ firstname + ' '+lastname+' you are '+str(age) + ' years old')

welcome('Allan','Doe',21)
welcome('Peter','Njuguna',25)
welcome('John','Wambui',77)


# create a function that takes two numbers and performs the  summation and then displays the summmation
def totals(num1,num2):
    sum=num1+num2
    print('The sum is '+str(sum))

totals(10,10)
totals(20,20)
totals(10,14)


def multiply(num1,num2):
    result=num1*num2
    return result

print(multiply(10,20))
print(multiply(5,5))
print(multiply(12,12))


def add_five(age):
    new_age=age+5
    return new_age

print(add_five(36))


def promoted(name,age):
    if age >5 and age<=7:
        return f"{name} You are {age} years old ,promoted to grade 1"

    elif age==7:
        return f"{name} You are {age} years old, promoted to grade 2"

    elif age>8 and age<10:
        return f"{name} You are {age} years old, promoted to grade 3"

    else:
        return f"{name} You are {age} years old,promoted to grade 4"



print(promoted('John',9))
print(promoted('Mary',45))
print(promoted('Anjeller',50))
print(promoted('Tom',34))



# create a function called greet that takes a persons name as an argument and returns a greeting message .If the name is 'Alice' or 'Bob' then it
# returns a personalized greeting .For any other name,it should return a generic greeting.

# &&-and ||-or you can use alternatively

def greet(name):
    if name == 'Alice' or name == 'Bob':
        return f"Hello {name} ! welcome "

    else:
        return " Hello,welcome "


print(greet('Alice'))
print(greet('Bob'))
print(greet('Renson'))
print(greet('Sarah'))













