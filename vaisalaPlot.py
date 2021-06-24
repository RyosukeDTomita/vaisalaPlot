##########################################################################
# Name: vaisalaPlot.py
#
# Make VAISALA like graph.
#
# Usage: python3 vaisalaPlot.py -i <input data>
#
# Author: Ryosuke Tomita
# Date: 2021/06/20
##########################################################################
import os
import re
import numpy as np
import matplotlib.pyplot as plt
import argparse
#made by tomita
from readcsv import readcsv

def getdateTime(data):
    matchObj = re.search('2.*[0-9]',str(data))
    return matchObj.group()

#-------parser setting-------
parser = argparse.ArgumentParser()
parser.add_argument("-i","--input",help="Select input file",type=str)
args = parser.parse_args()
data = args.input
#-------parameter setting-------
HOME = os.getenv("HOME")
datetime = getdateTime(data)
figName = ("./fig/" + datetime)
linestyle=["solid","dashed","dashdot","dotted"]

x1Header = "Temp"
x2Header = "RH"
x3Header = "P"
yHeader = "HeightMSL"

#-------read csv-------
readcsv = readcsv(data)
df = readcsv.df
x1 = readcsv[x1Header]
x2 = readcsv[x2Header]
x3 = readcsv[x3Header]
y  = readcsv[yHeader]
x1label = readcsv.getLabel(x1Header)
x2label = readcsv.getLabel(x2Header)
x3label = readcsv.getLabel(x3Header)
ylabel = readcsv.getLabel(yHeader)
print(datetime)

U = readcsv["Ecomp"]
V = readcsv["Ncomp"]
H = readcsv["HeightMSL"]
#-----figure-----
plt.rcParams['xtick.direction'] = 'in' # x軸(第一軸)の目盛りの向きを内側に設定
fig = plt.figure(figsize = (9,6))
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()
ax3 = ax1.twiny()

# ax1 (default is Temp)
color1='r'
ax1.plot(x1,y,
        label= x1Header,
        color= color1,
        linestyle=linestyle[0],
        linewidth = 1.0)
ax1.set_xlabel(x1label,
            fontsize=20,)
ax1.set_xlabel(x1label,fontsize=10,)
ax1.xaxis.set_label_coords(0.5,-0.04)
ax1.set_ylabel(ylabel,fontsize=10,)
ax1.spines["bottom"].set_color(color1)
ax1.spines["bottom"].set_linewidth(2.5)
ax1.xaxis.label.set_color(color1)
ax1.tick_params(axis = 'x', colors =color1)
# grid setting
ax1.xaxis.grid(True, which = 'major', linestyle = '-', color = '#CFCFCF')
ax1.yaxis.grid(True, which = 'major', linestyle = '-', color = '#CFCFCF')
ax1.set_axisbelow(True)

# ax2 (default is RH)
plt.rcParams['xtick.direction'] = 'out' # x軸(第二,第三軸)の目盛りを内向きに設定
color2='g'

ax2.plot(x2,y,
        label= x2Header,
        color= color2,
        linestyle=linestyle[0],
        linewidth = 1.0)
ax2.set_xlabel(x2label,
            fontsize=10,)
ax2.xaxis.set_label_coords(0.5,-0.17)
ax2.set_xticks(np.linspace(0,100,6),minor=True)
ax2.spines["top"].set_position(("axes",-0.12))
ax2.spines["top"].set_color(color2)
ax2.xaxis.label.set_color(color2)
ax2.tick_params(axis = 'x', colors =color2)

# ax3 (default is Pressure)
color3='b'
ax3.plot(x3,y,
        label= x3Header,
        color= color3,
        linestyle=linestyle[0],
        linewidth = 1.0)
ax3.set_xlabel(x3label,
            fontsize=10,)
ax3.xaxis.set_label_coords(0.5,-0.27)
ax3.set_xticks(np.linspace(1000,0,6),minor=True)
ax3.spines["top"].set_position(("axes",-0.22))
ax3.spines["top"].set_color(color3)
ax3.xaxis.label.set_color(color3)
ax3.tick_params(axis = 'x', colors =color3)

# wind profile
u,v,h = [],[],[]
for i in range(0,len(U),1):
    if i%150 == 0:
        u.append(U[i])
        v.append(V[i])
        h.append(H[i])
zero = np.zeros(len(h)) + max(x1) -1
ax1.barbs(zero,h,u,v)

# legend
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
h3, l3 = ax3.get_legend_handles_labels()
ax1.legend(h1 + h2 +h3, l1 + l2 + l3, loc='upper left')
fig.savefig(figName,bbox_inches="tight",pad_inches=0.5)
