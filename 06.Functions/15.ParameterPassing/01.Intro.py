# 1. Python uses a mechanism, which is known as "call-by-object" or "call-by-object-referenece"
# 2. The following rules must be considered:
#    a. Mutable obbjects can be changed within a method.(list, dict)
#    b. but if I rebind the reference in the method, the outer reference will still point to the original object
#    c. Immutable object can not be changed within a method.
#    d. But Immutable object CONTAINED WITHIN a mutable object can be re-assigned within a method.

# also, one more case of being careful with these two expression a+=b and a = a + b for mutable types.
# a += b has an effect onthe passed argument while the latter has not.  

