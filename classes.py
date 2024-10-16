# you must name a class using uppercase for the first letter
class Student:
    first_name='John'
    last_name='Kamau'
    gender='Male'
    age=23


 # this second class uses a constructor function ,a fn inside a class,,init fn allows you to define dynamic properties

class Person:
    def __init__(self,name, gender,marital_status,residence):
        self.name=name
        self.gender=gender
        self.marital_status=marital_status
        self.residence=residence

    # A class can contain a function within it
    # A fn inside a class is called a method
    # ensure the method below is indented to the right,same pos as the above fn

    def salutation(self):
        print(f'Hello {self.name},you are {self.marital_status}')


    def full_name(self):
        return f'My name is {self.name}'

# INHERITANCE

# create a class animal and its two instances and one method
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def mnyama(self ):
        return f'I am a {self.name} and my species is {self.species}'

class Carnivore(Animal):
    def __init__(self,name,species,region_found):
        super().__init__(name,species)
        self.region_found=region_found

    def wild(self):
        return f'I am found in {self.region_found}'




class Herbivore (Animal):
    def __init__(self,name,species,life_expectancy,predators):
        super().__init__(name,species)
        self.life_expectancy=life_expectancy
        self.predators=predators


# Parent class
class Employee():
    # constructor
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender

    def display(self):
        return f'{self.name} is {self.age} years old'


 # Manager is a child class,Employee is the parent class
 # we are inheriting name,age,salary and gender
 # we use a super function super()-which ones  we want to inherit from the parent
class Manager(Employee):
    def __init__(self,name,age,salary,gender,education_level):
        super().__init__(name,age,salary,gender)
        self.education_level=education_level

# Developer-child class,Employee-parent class
# super only contains the properties you have inherited
class Developer(Employee):
    def __init__(self,name,age,salary,gender,programming_language):
        super().__init__(name,age,salary,gender)
        self.programming_language=programming_language
