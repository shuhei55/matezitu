import math as m
import numpy as np

R = 8.3144598 
F = 96500
h = m.log(0.2/1.0)

T = np.array([1023,1073,1123,1173])
#for i in range(T):
#    i += 273
G = np.array([-148300,-144100,-139900,-135700])
E = np.array([-256.3,-261.4,-266.6,-270.7])
E4 = np.array([-210.8,-201.0,-189.5,-181.5])
print((G + 2 * F * E)/1000)
print((G + 2 * F * E4 - 3 * G + 2 * F * E)/1000)
