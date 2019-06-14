import math as m
import numpy as np

R = 8.3144598 
F = 96500
h = m.log(0.2/1.0)

T = np.array([1000, 950,900,850,800,750,700,650,600])
#for i in range(T):
#    i += 273
T += 273
print((R*T*h)/(4 * F) * 1000)
