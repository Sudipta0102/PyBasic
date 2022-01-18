import copy


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, emp):
        self.boss = boss
        self.emp = emp


boss1 = Person("bossman", 12)
emp1 = Person("blehman", 30)

company = Company(boss1, emp1)

# print(company.emp.name)

company_shallow_copy = copy.copy(company)

company_shallow_copy.boss.name = 'Ass'

# now both are supposed change as this is shallow copy and a nested object.
print(company.boss.name)
print(company_shallow_copy.boss.name)

# _________________________________________________________________________

boss1 = Person("bossman", 12)
emp1 = Person("blehman", 30)
company1 = Company(boss1, emp1)

#print(company1.boss.name)

company_deep_copy = copy.deepcopy(company1)
company_deep_copy.boss.name = 'Ass'

# Now only later is supposed to change keeping the original one intact.
print(company1.boss.name)
print(company_deep_copy.boss.name)

