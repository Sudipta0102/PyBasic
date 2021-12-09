# Operator Function needs to 'import' operator interface
import operator

a = 4
b = 3

# add()
print("add:", operator.add(a, b))

# subtract
print("subtract:", operator.sub(a, b))

# multiply
print("multiply:", operator.mul(a, b))

# True Division
print("True Division:", operator.truediv(a, b))

# Floor Division
print("Floor Division:", operator.floordiv(a, b))

# Power
print("Power:", operator.pow(a, b))
# operation a**b

# modulus
print("Mod:", operator.mod(a, b))

# less than
print("a less than b:", operator.lt(a, b))

# less than or equal
print("a less than or equal b:", operator.le(a, b))

# greater than
print("a greater than b:", operator.gt(a, b))

# greater than or equal
print("a greater than or equal b:", operator.ge(a, b))

# equal to or not
print("a equal to b:", operator.eq(a, b))

# not equal to equal [True if not equal]
if(operator.ne(a, b)):
    print("a not equal to b:", operator.ne(a, b))
else:
    print("a equal to b", operator.ne(a, b)) 

#---------------------------------------------------------

# assigning item at an index in a container like list etc.
list = [1, 2, 3, 4, 5]

print("List before setting another item")       
print(list)
operator.setitem(list, 4, 6)
print("List after setting another item")       
print(list)

# deleting item
operator.delitem(list, 3)
print("List after deleting another item")
print(list)

# Fetching another item
print("Getting the 0th index value:")
print(operator.getitem(list, 0))

#---------------------------------------------------------------

list1 = [1, 5, 6, 7, 5]

# you can just get a slice of the list and set items for that.
print("before setting:", list1)
operator.setitem(list1, slice(1, 4), [2, 3, 4])
print("after setting: ", list1)

# also items can be deleted in slice
operator.delitem(list1, slice(1,3))
print("after deleting:", list1)

# items can be fetched too
print(operator.getitem(list1, slice(0, 2)))

#----------------------------------------------------------------

# concat two container
list = [1,2,3]
list1 = [4,5,6]

print(operator.concat(list, list1))
# or
s = "Me"
s1 = "ew"
print(operator.concat(s, s1))

# check obj1 contains obj2 or not
print(operator.contains(list, 1)) 

#-------------------------------------------------------------

a = 1
b = 0

# bitwise AND
print(operator.and_(a, b))

# bitwise OR
print(operator.or_(a, b))

# bitwise XOR
print(operator.xor(a, b))

# values can be inverted
print(operator.invert(a))
