import string
import secrets

# Generate a ten-character alphanumeric password with
# 1. at least one lowercase character,
# 2. at least one uppercase character, and
# 3. at least three digits:

alphanums = string.ascii_letters + string.digits

# the way to do that is:
# 1. generate 10 char random string,
# 2. check for above three conditions,
# 3. if met, break.

while True:
    password = ''.join(secrets.choice(alphanums) for i in range(10))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        print(password)
        break
