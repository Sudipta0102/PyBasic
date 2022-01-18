# 1. In pyhon, assignment operator, like obj_a = obj_b do not create real copies.
# it only creates a new variable with same reference
# 2. So, when you want to make actual copies of mutable objects like list, dict
# and also want to modify the copies without affecting the original, you would have
# to be careful.
# 3. for 'real' copies we can use the 'copy' module.
# 4. for COMPOUND AND NESTED OBJECTS (e.g. nested lists or dicts) and custom objects,
# there are is an important difference between shallow and deep copying;-
#
#   a. SHALLOW copies:
#       -> Only one level deep.
#       -> creates a new collection object and populates it with the reference to the
# nested objects.
#       -> the above point means, modifying a copied nested object which is deeper than
# one level will end up affecting the original copy.
#
#   b. DEEP copies:
#       -> a fully independent clone.
#       -> creates a new collection object and then recursively populates it with copies
# of nested objects found in the original.

