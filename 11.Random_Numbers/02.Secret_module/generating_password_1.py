# generating an alphanumeric password:

import string
import secrets

alphanum = string.ascii_letters + string.digits

print(alphanum)

# this way, it's a list
password = [secrets.choice(alphanum) for i in range(8)]
# this way, it's a generator object.
password1 = (secrets.choice(alphanum) for i in range(8))


# can join the generator object, will give you eight char password
password2 = ''.join(secrets.choice(alphanum) for i in range(8))
print(password2)


# important note:
# Applications should not store passwords in a recoverable format, whether plain text or encrypted.
# They should be salted and hashed using a cryptographically-strong one-way (irreversible) hash function.






