from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import os
wd = os.chdir('/Users/larslarson/Documents/School/CU/Research/TADD/Data/2022-03-04')

filepaths = [f for f in os.listdir(wd) if f.endswith('.csv')]
df = pd.concat(map(pd.read_csv, filepaths),axis='columns')

file_names = []
data_frames = []
locations = []
for filename in filepaths:
    name = os.path.splitext(filename)[0]
    file_names.append(name)
    df = pd.read_csv(filename, header=None)
    name = name.partition("y")[2]
    location = name.partition("_")[0]
    location = int(location)
    df.rename(columns={1: name}, inplace=True)
    data_frames.append(df)
    locations.append(location)
combined = pd.concat(data_frames, axis=1)
#print(locations)
volts = (combined.iloc[:,1:96:2])
volts = volts.iloc[1:-1,:]
volts = volts.astype(float)
volts = volts.iloc[610:1220,:]
vmean = volts.mean(axis=0,skipna = True)
#print("mean = ", vmean)
#print(volts)
plt.figure(1)
for i, col in enumerate(volts.columns):
    volts[col].plot()
    

#locations.sort()
plt.figure(2)
basev1 = pd.read_csv('/Users/larslarson/Documents/School/CU/Research/TADD/Data/x1m_CL_zp8cm_base.csv')
basev1 = basev1.iloc[:,1]
basev1 = np.mean(basev1)
basev2 = pd.read_csv('/Users/larslarson/Documents/School/CU/Research/TADD/Data/x1m_CL_zp8cm_base_v2.csv')
basev2 = basev2.iloc[:,1]
basev2 = np.mean(basev2)
plt.plot(locations,vmean,'.')
plt.hlines(basev1,-32,32,'k')
plt.hlines(basev2,-32,32)
plt.xlabel('y location (cm)')
plt.ylabel('volts')
#print(volts.iloc[1000:1220,:])
plt.show()


