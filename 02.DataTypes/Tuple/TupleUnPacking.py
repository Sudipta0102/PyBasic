from typing import Tuple


Tuple1 = ("I","am","for","real")
a,b,c,d = Tuple1
# 1,2,3,4 = Tuple1
print(d)
print()
Tuple2 = ('pseudoFunc', '55', 'Venice')
name, age, place = Tuple2
print(name)
print(age)
print(place)

# one more usage:
# the general notion is your number of elements should be equal to number of elements in the tuple.
# otherwise you will get a 'too many vales to unpack' or 'Not enough values to unpack' error.

# But, if that's your desired effect, you can get around with * operator. Let's look at the example:
student1 = ("PseudoFunc", 90, 92, 76, 98, 89, 'VII')
student2 = ("BustyBabe", 90, 92, 76, 98, 89, 'IX')

name, *marks, standard = student1

print(name)
print(marks) # Now it's a list of marks.
print(standard)


# You can use this in various creative ways. Please keep in touch.

