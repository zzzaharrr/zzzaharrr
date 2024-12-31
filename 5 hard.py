def f25(n):
    s = ''
    alp = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        s = alp[n%25]+s
        n //= 25
    return s
res = []
for n in range(1,100000):
    s = f25(n)
    if any(x in s for x in 'abcdefghijklmno'):
        for x in 'abcdefghijklmno': s = s.replace(x,'0')
    else:
        s = s.replace('0','o')
        s = s.replace('1','l')
        s = s.replace('2','d')
        s = s.replace('3','e')
        s = s.replace('4','f')
        s = s.replace('5','c')
        s = s.replace('6','b')
        s = s.replace('7','j')
        s = s.replace('8','i')
        s = s.replace('9','g')
    r = int(s,25)
    if r<=202050: res += [r]
print(max(res))
