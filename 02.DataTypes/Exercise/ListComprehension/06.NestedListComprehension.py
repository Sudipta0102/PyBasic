# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by
# any single digit besides 1 (2–9)

# 1.
# let's build a matrix in normal way
matrix = []
for i in range(5):
    matrix.append([])
    for j in range(1, 5):
        matrix[i].append(j)

print(matrix)
# using nested list comprehension
matrix = [[j for j in range(1, 5)] for i in range(5)]
print(matrix)


# 2. flattening the matrix
matrix = [[1, 2, 3, 3.5], [4, 5, 6], [7, 8, 9]]
# normal way
flatten_matrix = []

for sublist in matrix:
    for val in sublist:
        flatten_matrix.append(val)

print(flatten_matrix)

# comprehension way
flatten_matrix1 = [val for sublist in matrix for val in sublist]
print(flatten_matrix1)


# 3. I want to flatten a given 2-D list and only include those strings whose lengths are less than 6
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
flatten_planets = []
# Normal way
for sublist_planet in planets:
    for planet in sublist_planet:
        if len(planet)<6:
            flatten_planets.append(planet)

print(flatten_planets)

# comprehension way
flatten_planets1 = [planet for sublist_planet in planets for planet in sublist_planet if len(planet) < 6]
print(flatten_planets1)


# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by
# any single digit besides 1 (2–9)

# Normal way
result_list = []
flag = 0
for val in range(1, 10001):
    for divisor_val in range(2, 10):
        if val % divisor_val != 0:
            flag = 1
    if flag == 0:
        result_list.append(val)
    else:
        flag = 0

print(result_list)

# comprehension way
nums = [num for num in range(1, 20)]

# doesn't work
result_list1 = [num for num in range(1, 20) if True in [True for divisor in range(3, 5) if num % divisor == 0]]

print(result_list1)

