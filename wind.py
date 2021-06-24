import matplotlib.pyplot as plt
import numpy as np
# made by tomita
from readcsv import readcsv

fig = plt.figure(figsize = (4.5,7))
ax = fig.add_subplot(111)
data = "./data/mirai_rs41_20210619_2330.txt"
u,v,h = [],[],[]

readcsv = readcsv(data)
df = readcsv.df
U = readcsv["Ecomp"]
V = readcsv["Ncomp"]
H = readcsv["HeightMSL"]
for i in range(0,len(U),1):
    if i%150 == 0:
        u.append(U[i])
        v.append(V[i])
        h.append(H[i])
zero = np.zeros(len(h))
ax.barbs(zero,h,u,v)
ax.tick_params(labelbottom=False,
               labelleft=True,
               labelright=False,
               labeltop=False)
ax.tick_params(bottom=False,
               left=True,
               right=False,
               top=False)

plt.show()
