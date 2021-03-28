from sys import stdin
input = stdin.readline
s = input().strip()
alpha = 'LMS'
ind = [s.count('L')]
ind.append(ind[0] + s.count('M'))
ind.append(ind[-1] + s.count('S'))
ct = [
    (s[:ind[0]].count('M'), s[:ind[0]].count('S')),
    (s[ind[0]:ind[1]].count('L'), s[ind[0]:ind[1]].count('S')),
    (s[ind[1]:].count('L'), s[ind[1]:].count('M'))
        ]
ans = 0
ans += min(ct[0][0], ct[1][0]) 
ans += min(ct[0][1], ct[2][0])
ans += min(ct[1][1], ct[2][1])
#print(ans)
sum = 0
for i in ct:
    sum += i[0] + i[1]
ans += ((sum - ans*2)/3)*2
print(int(ans))


