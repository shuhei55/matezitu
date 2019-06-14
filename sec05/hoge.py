import math as m
x = [4.0,4.8,3.6,3.2,4.2]
y = [0.8,0.6,0.4,0.6,0.5]

ave = 0

for i in y:
    ave += i

ave = ave / 5
print(ave)
hoge = 0
for i in y:
    hoge += (i - ave)*(i - ave)
hoge /= 5
print(m.sqrt(hoge))
