##########################################################################
# Name: readcsv.py
#
# Read csvfile. If file is txt, then convert to csv.
#
# Usage:
#
# Author: Ryosuke Tomita
# Date: 2021/06/20
##########################################################################
import pandas as pd
import csv
import re

class readcsv:
    def __init__(self,data):
        def getCsv(data):
            df = pd.read_csv(data,header=13,)
            self.units = (df.loc[0])
            df_droped = df.drop(0)
            self.df = df_droped.reset_index(drop=True)

        if re.match('.*csv$',data):
            getCsv(data)
            return None
        elif re.match('.*txt$',data):
# convert txt to csv
            csvdata = data.replace("txt","csv")
            with open(data, newline='',encoding='s-jis') as f_in, \
                open(csvdata, mode="w", newline='') as f_out:
                reader = csv.reader(f_in,
                        delimiter='\t',
                        skipinitialspace=True)
                writer = csv.writer(f_out)
                writer.writerows(reader)
            getCsv(csvdata)
            return None
        else:
            print("file extension error")
            return None
    def __getitem__(self,header):
        self.cutdf = self.df.loc[:,header]
        try:
            self.cutdf = self.cutdf.astype(float)
        except ValueError:
            print("Datas are not integer or float.")
        if header == "Temp":
            self.cutdf += -273.15
        return self.cutdf

    def __getattr__(self,attrName):
        if   attrName == "df":
            return self.df
        elif attrName == "headers":
            return self.df.columns
        elif attrName == "units":
            return self.units
    def getLabel(self,header):
        if header == "Temp":
            label = (header + " ℃")
        else:
            label = (header + " " + self.units.loc[header])
        return label
