import re

test_str = "jeeks4feeks is No. 1 4 heeks"
res = len(re.findall(r'\d+', test_str))
print(res)

