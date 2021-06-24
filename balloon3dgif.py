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
import itertools
from matplotlib.collections import LineCollection, PolyCollection
import cartopy.crs as ccrs
import cartopy.feature
from cartopy.mpl.patch import geos_to_path
# make by tomita
from readcsv import readcsv
data = "./data/mirai_rs41_20210619_2330.txt"
readcsv = readcsv(data)
df = readcsv.df
lat = readcsv["Lat"]
lon = readcsv["Lon"]
h = readcsv["HeightMSL"]

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.set_xlim(132,135)
ax.set_ylim(32,35.0)
ax.set_zlim(0,30000)
ax.set_xlabel("lon")
ax.set_ylabel("lat")
ax.set_zlabel("HeightMSL")
ax.set_facecolor('w')

# 地図のためのaxisを設定
proj_ax = plt.figure().add_subplot(111, projection=ccrs.PlateCarree())
proj_ax.set_xlim(ax.get_xlim())
proj_ax.set_ylim(ax.get_ylim())
concat = lambda iterable: list(itertools.chain.from_iterable(iterable))
# geometryの取得
target_projection = proj_ax.projection
feature = cartopy.feature.NaturalEarthFeature('physical', 'land', '10m')
geoms = feature.geometries()
# 領域の取得
boundary = proj_ax._get_extent_geom()
# 投影方法の変換
geoms = [target_projection.project_geometry(geom, feature.crs) for geom in geoms]

# invalid な geometryの排除
#geoms2 = []
#for i in range(len(geoms)) :
#    if geoms[i].is_valid :
#        geoms2.append(geoms[i])
#geoms = geoms2

# intersection(plot領域から地図がはみ出す)
geoms = [boundary.intersection(geom) for geom in geoms]
# geometry to path to polygon to collection
paths = concat(geos_to_path(geom) for geom in geoms)
polys = concat(path.to_polygons() for path in paths)
lc = PolyCollection(polys, edgecolor='black', facecolor='green', closed=True, alpha=0.2)

ax.add_collection3d(lc, zs=0) #zsを変えると日本地図の位置が変わる
ax.view_init(elev=30, azim=-120)

ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0)) #背景を透明にする
ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))

for i in range(0,len(h),50):
    ax.plot(lon[0:i],lat[0:i],h[0:i],color="#1e90ff")
    figurName = ("./gif/ballon" + str(i))
    fig.savefig(figurName,bbox_inches="tight",pad_inches=0.5)
