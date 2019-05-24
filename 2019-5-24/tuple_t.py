t = tuple('xiaomi')
print(t)

addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname, domain)

s = 'abc'
t = [0, 1, 2]
for  pair in zip(s, t):
    print(pair)