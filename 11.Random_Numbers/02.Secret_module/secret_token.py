import secrets
# this generated token can be used for so many things like, password reset, hard to guess URLs etc.
#

# for all three methods, when no arg is provided, then it's reasonable default.


print(secrets.token_bytes())
print(secrets.token_bytes(32))
print('-'*32)
print(secrets.token_hex())
print(secrets.token_hex(32))
print('-'*32)
print(secrets.token_urlsafe())
print(secrets.token_urlsafe(32))


url = 'https://daddycomedaddygo.com/reset=' + secrets.token_urlsafe(32)

print(url)
