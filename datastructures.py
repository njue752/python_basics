
# lists
# a list is identified using square brackets
employees=['Peter','John','Smith','Esther']
print(employees)
# to identify items inside a list
# you start at index zero incrementally,index one,index two etc
print(employees[2])
print(employees[0])
# printing a range of values
print(employees[1:4])
# printing peter and john only
print(employees[0:2])
# changing an item inside a list
# eg changing the first value peter to another name
employees[0]='Alex'
print(employees)
employees[3]='Jackline'
print(employees)


# append adds a value to the list
employees.append('William')
print(employees)

# inserting a value at a specific point within the list
# type 0 and '' ,will appear by default
employees.insert(0,'Susan')
print(employees)

employees.extend(['Pauline','Doe','Koi'])
print(employees)
# append only adds one value to a list,extend adds more than one value to the list,at the end,use insert for a specific point

marks=[234,543,564,543,987]
# getting the maximum,minimum and total
print(max(marks))
print(min(marks))
print(sum(marks))

# tuples
# a tuple uses the ordinary brackets
languages=('Java','Python','Javascript')
print(languages)
print(languages[1])
print(languages[1:4])
# a tuple does not allow you to change an item inside the tuple
# languages[0]='Kotlin' trying to change the index0 item from java to kotlin,not possible,will raise an error


# sets
# a set uses the curly braces
# a set is not ordered,it has random items in the set
mysets={'Python','Java','Javascript','Php'}
print(mysets)
# printing a specific item

word='Java'
if word in mysets:
    print(word)
  # alternatively

if 'Java' in mysets:
    print('Java')

if 'Python' in mysets:
    print('Python')
 # displaying an item not on the set
if 'kotlin' in mysets:
    print('kotlin')
else:
    print('not  here')

# add adds anywhere
mysets.add('Charles')
# update adds at the first position
mysets.update(['C sharp'])

mysets.remove('Charles')


# dictionary
# a dictionary is always in key value pairs,uses curly braces like a set
# there is no indexing in a dictionary
mydictionary={
    'Title':'The code',
    'Author':'John Doe',
    'Publisher':'KLB',
    'Year published': 2000
}
print(mydictionary)

print(mydictionary['Publisher'])
# adding an item inside the dictionary,the key and the value
mydictionary['version'] = 'Three'
print(mydictionary)

if'version' in mydictionary:
    print("Yes it is present here")
else:
    print("No it is not present here")


    # create a student dictionary with all the necessary items and check existence of  the gender of a student

details={
    'Firstname':'Martin',
    'Lastname':'Njue',
    'YOB':2016,
    'Course':'MIT',
    'Next of kin':'Mary Wame',
    'gender':'Male'

}
print(details)

if 'gender' in details:
    print('gender is present')
else:
    print('gender is not present')
















