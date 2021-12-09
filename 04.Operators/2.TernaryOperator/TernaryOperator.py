a, b = 10, 20

# this thing goes like this:
# [on-true] if [expression] else [on-false]
min = a if a < b else b
print(min)

# ternary operator in tuples
# the formatting is :
# (if_expr_false, if_expr_true) [expr]
print((b,a)[a<b])

# ternary operators on dictionary
# if expression is true then true key's value will print
# if false then false key's value will print
print({True: a, False: b}[a<b])

# ternary operators on lambda
print((lambda: b, lambda: a)[a<b]())
# things to remember: I dunno a thing about lambda