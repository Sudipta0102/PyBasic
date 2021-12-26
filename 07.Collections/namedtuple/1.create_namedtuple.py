from collections import namedtuple

Student = namedtuple('Student', 'name, age, city')

student1 = Student('ami', 82, 'bleh')

print(student1)
print(student1._fields)
print(student1.name)
print(student1.age)
print(student1.city)

City = namedtuple('City', 'polulation, location')
city1 = City(12, 'bleh')

# basically, It created a class named as first argument with attributes mentioned argument in second element

# i dunno what to do with this information called namedtuple
