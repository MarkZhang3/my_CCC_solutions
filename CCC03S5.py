from sys import stdin, exit
input = stdin.readline
for case in range(10):
    n = int(input())
    ans = 0
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    if n%2 != 0:
        print(0)
        continue
    subarr = []
    for i in range(n//2):
        x1, y1 = points[i]
        x2, y2 = points[n//2 + i]
        #print(x1, y1)
        #print(x2, y2)
        m, mp = 999999999999, 999999999999 #999999999999 = UND
        if (y1-y2) != 0:
            mp = -1 * (x1-x2) / (y1-y2) 
        if (x1-x2) != 0:
            m = (1/mp)*(-1)
        subarr = points[:i] + points[n//2+i+1:]
        #print(subarr)
        f = 1
        #print(mp)
        yint1 = y1-(m*x1)
        #print('eqn',m, yint1)
        for j in range(i+1, i + n//2):
            a, b = points[j] 
            #eqn: y = mx + b, y = mp + b 
            yint2 = b - (mp * a)
            POIx = (yint2 - yint1) / (m - mp)
            POIy = m * (POIx) + yint1 
            dx, dy = POIx - a, POIy - b  
            newp = (round(POIx+dx), round(POIy+dy))
            #print(a, b, newp, POIx, POIy, m, mp)
            if newp not in subarr:
                f = 0 
                break
        ans += f 
    print(ans)