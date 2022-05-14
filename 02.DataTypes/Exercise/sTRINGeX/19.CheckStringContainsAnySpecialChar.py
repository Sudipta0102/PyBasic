import re

s = "GeeksForGeeks"

reg = re.compile("[@_!#$%^&*()<>?/\|}{~:]")

if reg.search(s) is None:
    print("ok")
else:
    print("not ok")
