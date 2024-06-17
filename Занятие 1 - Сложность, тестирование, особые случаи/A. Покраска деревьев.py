p, v = map(int, input().split())
q, m = map(int, input().split())

v1 = p-v
v2 = p+v
m1 = q-m
m2 = q+m 

if min(v2, m2) < max(v1, m1):
    print(v2 - v1 + 1 + m2 - m1 + 1)
else:
    print(max(v2, m2) - min(v1, m1) + 1)


