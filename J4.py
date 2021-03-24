from sys import stdin
input = stdin.readline
s = input().strip()
num = [0, 0, 0]
alph = "LMS"
for i in s:
    num[alph.index(i)] += 1 
num[1] += num[0]
num[2] += num[1]
ans = 0
for i in range(num[0]):
    if s[i] == 'M':
        if 'L' in s[num[0]:num[1]]:
            ans += 1 
        else:
            ans += 2
    elif s[i] == 'S':
        if 'L' in s[num[1]:]:
            ans += 1 
        else:
            ans += 2 
for i in range(num[0], num[1]):
    if s[i] == 'S':
        if 'S' in s[num[0]:num[1]]:
            ans += 1 
print(s[num[0]:num[1]], s[num[1]:])
print(ans)