##########################################################################
# Name: balloonLocation.py
#
# Plot zonde ballon gps location data.
#
# Usage: python3 ballonLocation.py
#
# Author: Ryosuke Tomita
# Date: 2021/06/21
##########################################################################
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import cartopy.crs as ccrs
import cartopy.feature as cfea
from cartopy.mpl.ticker import LatitudeFormatter,LongitudeFormatter
# made by Tomita
from readcsv import readcsv

HOME = os.getenv("HOME")
dataDir = os.path.join(HOME + "/zonde/data")
PWD = os.getcwd()
data = os.path.join(dataDir + "/mirai_rs41_20210619_2330.txt")
readcsv = readcsv(data)
df = readcsv.df
lat = readcsv["Lat"]
lon = readcsv["Lon"]


# map
fig = plt.figure(figsize=(36,24),facecolor='w')
ax = fig.add_subplot(1,1,1,
        projection=ccrs.PlateCarree(central_longitude=0.0))
ax.set_global()
ax.coastlines()
dlon,dlat = 1,1 #punctuation
xticks = np.arange(-180,180.1,dlon)
yticks = np.arange(-90,90.1,dlat)
ax.set_xticks(xticks,crs=ccrs.PlateCarree())
ax.set_yticks(yticks,crs=ccrs.PlateCarree())
latfmt = LatitudeFormatter() #axis = degree
lonfmt = LongitudeFormatter(zero_direction_label=True) # No NS mark 0 degree
ax.xaxis.set_major_formatter(lonfmt)
ax.yaxis.set_major_formatter(latfmt)
ax.axes.tick_params(labelsize=12)
ax.plot(lon,lat,'bo',
        markersize      = 5,
        color           = '#ff1493',
        markeredgewidth = 0.3,
        markeredgecolor = 'gray')
ax.add_feature(cfea.LAND,color='#2f4f4f')
ax.add_feature(cfea.OCEAN,color='#4682b4')

grid = ax.gridlines(crs       = ccrs.PlateCarree(),
                  draw_labels = False,
                  linewidth   = 1,
                  alpha       = 0.8,
                  color       = 'k')
ax.set_xlim(130,135)
ax.set_ylim(30,35)
grid.xlocator = mticker.FixedLocator(xticks)
grid.ylocator = mticker.FixedLocator(yticks)

fig.savefig("./fig/balloon",bbox_inches="tight",pad_inches=0.5)

