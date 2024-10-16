# import Student from classes ignore use the alt below
# import all the classes at the top
from classes import Student
from classes import Person
from classes import Animal
from classes import Carnivore
from classes import Herbivore
from classes import  Employee
from classes import Manager
from classes import Developer





# student1 is an object/instance,Student is the class
student1=Student()
print(student1.first_name)
print(student1.last_name)
print(student1.gender)
print(student1.age)


person1=Person('Alex','Male','married','Nairobi')
print(person1.name)
print(person1.gender)
print(person1.marital_status)
print(person1.residence)

person1.salutation()
print(person1.full_name())

# To print out everything
print(f'Name:{person1.name},Gender:{person1.gender},Marital_status:{person1.marital_status},Residence:{person1.residence}')


person2=Person('Alice','Female','Single','Kisumu')
print(person2.name)
print(person2.gender)
print(person2.marital_status)
print(person2.residence)

person2.salutation()

person3=Person('Sarah','Female','Divorced','Samburu')
print(person3.name)
print(person3.gender)
print(person3.marital_status)
print(person3.residence)
person3.salutation()

person4=Person('Dickson','Male','Married','Kwale')
print(person4.name)
print(person4.gender)
print(person4.marital_status)
print(person4.residence)
person4.salutation()



animal1=Animal('Lion','Carnivore')
print(animal1.name)
print(animal1.species)
animal1.mnyama()

animal2=Animal('Gazelle','Herbivore')
print(animal2.name)
print(animal2.species)
animal2.mnyama()

animal3=Animal('Hippo','Herbivore')
print(animal3.name)
print(animal3.species)
animal3.mnyama()

animal4=Animal('Gorilla','Primate')
print(animal4.name)
print(animal4.species)
animal4.mnyama()




# inheritance implementation
employee1=Employee('Judy',34,100000,'Female')
print(employee1.name)
print(employee1.age)
print(employee1.salary)
print(employee1.gender)
print(f'Name:{employee1.name},Age:{employee1.age},Salary:{employee1.salary},Gender:{employee1.gender}')

# objects/instances that are inheriting

manager1=Manager('Paul',35,250000,'Male','Degree')
print(f'Name:{manager1.name},Age:{manager1.age},Salary:{manager1.salary},Gender:{manager1.gender},Education:{manager1.education_level}')


developer1=Developer('Thomas',34,560000,'Male','Python')
print(developer1.display())

developer2=Developer('Ann',24,'500000','Female','Kotlin')
print(developer2.display())

developer3=Developer('Esther',26,320000,'Female','JavaScript')

print(developer3.display())

# Output this statement Esther,Thomas and Ann are developers earning 320000,560000 and 500000 respectively.Their gender is Female,Male and Female.


print(f'Name:{developer1.name},{developer2.name} and {developer3.name}, are developers earning {developer1.salary},{developer2.salary} and {developer3.salary}'
      f' respectively.Their genders are  {developer1.gender},{developer2.gender},and {developer3.gender} respectively.')



mnyama1=Carnivore('Leopard','Carnivora','Africa')
print(f'I am a {mnyama1.name} , My species is {mnyama1.species} and my region is {mnyama1.region_found}')
print(mnyama1.mnyama())
print(mnyama1.wild())





mnyama2=Herbivore('Zebra','Herbivore',35,'Leopards')
print(f'I am a {mnyama2.name} , My species is {mnyama2.species} and my life expectancy  is {mnyama2.life_expectancy} years.My major '
      f'predators are {mnyama2.predators}.')


# javatpoint
# geeksforgeeks