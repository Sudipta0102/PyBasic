import secrets

# this is kinda self explanatory
a = secrets.randbelow(10)
print(a)

print(secrets.randbits(2))
# 00, 01, 10, 11
#  0,  1,  2,  3


print(secrets.token_urlsafe(64))
print(secrets.token_bytes(16))
print(secrets.token_hex(16))
