res = []
for n in range(1,2000):
    s = bin(n)[2:]
    if n%2!=0: s = s[::-1]+'10'
    else: s = (s+'01')[::-1]
    r = int(s,2)
    if r>2025: res += [r]
print(min(res))
