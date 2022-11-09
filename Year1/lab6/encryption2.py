s = '12345678'
t = iter(s)
print('-'.join(a+b for a,b in zip(t, t)))
