# problem statement:
# Phone formats can be
# 1. 415.555.4242 x99
# 2. (415) 555-4242 x99
# 3. 415-555-4242 x99
# extension part is optional. Find the given phone number is a valid one or not.

import re

# r""-> raw string
# so, what's the difference then?
pattern_obj = re.compile(r"\d{3}-\d{2}|\d{4}-\d{2}")
matcher_obj = pattern_obj.search('My number is 1000-22')
print(matcher_obj.group())

# \d{4}-\d{3}-\d{3}(x\d{1,2})?|\d{4}.\d{3}.\d{3}(x\d{1,2})?

