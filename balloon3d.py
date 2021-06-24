##########################################################################
# Name: balloon3d.py
#
# 3D plot of zonde ballon
#
# Usage: python3 ballon3d.py
#
# Author: Ryosuke Tomita
# Date: 2021/06/22
##########################################################################
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccr
from mpl_toolkits.mplot3d import Axes3D
# make by tomita
from readcsv import readcsv
data = "./data/mirai_rs41_20210619_2330.txt"
readcsv = readcsv(data)
df = readcsv.df
lat = readcsv["Lat"]
lon = readcsv["Lon"]
h = readcsv["HeightMSL"]

fig = plt.figure(figsize=(10,5),facecolor='w')
ax = Axes3D(fig)
ax.set_xlabel("lat")
ax.set_ylabel("long")
ax.set_zlabel("HeightMSL")
ax.set_facecolor('w')
ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.plot(lat,lon,h)
fig.savefig("./fig/balloon3d",bbox_inches="tight",pad_inches=0.5)
