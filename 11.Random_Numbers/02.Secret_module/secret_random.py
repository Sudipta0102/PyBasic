import secrets

# this is kinda self-explanatory
a = secrets.randbelow(10)
print(a)

# randbits(3) -> this arg means,
# 1. it will be a 3 bit number at the most
# 2. in this case, binary 111 (decimal-> 7) should be the upper limit.
#
print(secrets.randbits(3))
# 00, 01, 10, 11
#  0,  1,  2,  3




print(secrets.token_urlsafe(64))
print(secrets.token_bytes(16))
print(secrets.token_hex(16))
