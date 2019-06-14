import math as m
import sys

args = sys.argv

f = open(args[1],'r')
f2 = open('datas/alpha_beta_01_02.dat')

s = f.readlines()

s2 = f2.readlines()

alpha1=0 #0.1nm
alpha2=0
beta1=0

a = 0.40496 #nm
def get_d(h,k,l):
    return m.sqrt(1.0/((h**2+k**2+l**2)/a**2))

for i in range(len(s2)):
    if i == 1 or i == 0:
        continue
    alpha2 = float(s2[i].split()[0])
    alpha1 = float(s2[i].split()[1])
    beta1 = float(s2[i].split()[2])

riron = [[get_d(4,0,0),alpha1],[get_d(4,0,0),alpha2],[get_d(4,0,0),beta1],[get_d(3,3,1),beta1],[get_d(4,2,0),beta1]]
for i in riron:
    theta = m.asin(i[1] / (2.0*i[0]) * 0.1)
    #print(i[0],'nm',theta,'rad')

for i in range(len(s)):
    if i == 1 or i == 0:
        continue
    if i == 2:
        riron[2].append(float(s[i].split()[0]) * m.pi / 180 / 2)
    if i == 3:
        riron[3].append(float(s[i].split()[0]) * m.pi / 180 / 2)
    if i == 4:
        riron[0].append(float(s[i].split()[0]) * m.pi / 180 / 2)
    if i == 5:
        riron[1].append(float(s[i].split()[0]) * m.pi / 180 / 2)
    if i == 6:
        riron[4].append(float(s[i].split()[0]) * m.pi / 180 / 2)

print('d[nm]','d0','delta_d(d-d0)')
for i in riron:
    print(i[1] / 2.0 / m.sin(i[2]) * 0.1 ,i[0], i[1] / 2.0 / m.sin(i[2]) * 0.1 - i[0])


f.close()


