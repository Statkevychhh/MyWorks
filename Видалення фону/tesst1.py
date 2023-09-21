s = int(input('s'))
n = int(input('n'))
c = 0
s1 = 0
s2 = 0
arr = []
while c < n:
    arr.append(int(input('e')))
    c += 1

for x in arr:
    if s >= x:
         s -= x
         s1 += x
    elif s < x:
        s2 += x

print(s1, s2)