"""
Yasuhiko Komatsu
"""

import matlab.engine
import numpy as np
import pandas as pd
eng = matlab.engine.start_matlab()

#%%
file_name = 'GE_53_071222_C1_072922_C001H001S0011pts_Hiko'
trial_list = 1
example_file = eng.load(file_name+'.mat')['d']['data']

#%%
# define a function to extract the x and y coordinate from each entry
def get_x_coordinate(entry):
    return entry[0]
def get_y_coordinate(entry):
    return entry[1]

def get_coordinates(field):
    series = pd.Series(list(np.asarray(eng.getfield(example_file, field))))
    x_coord = series.apply(get_x_coordinate)
    y_coord = series.apply(get_y_coordinate)
    return x_coord, y_coord

Cdist_xcoord, Cdist_ycoord = get_coordinates("Cdist")
Cexten_xcoord, Cexten_ycoord = get_coordinates("Cexten")
Clump_xcoord, Clump_ycoord = get_coordinates("Clump")
CslideTop_xcoord, CslideTop_ycoord = get_coordinates("CslideTop")

Extensor_xcoord, Extensor_ycoord = get_coordinates("Extensor")

Latch_xcoord, Latch_ycoord = get_coordinates("Latch")

MDist_xcoord, MDist_ycoord = get_coordinates("MDist")
MLat_xcoord, MLat_ycoord = get_coordinates("MLat")
MProx_xcoord, MProx_ycoord = get_coordinates("MProx")

MVnotchP_xcoord, MVnotchP_ycoord = get_coordinates("MVnotchP")
MVtip_xcoord, MVtip_ycoord = get_coordinates("MVtip")
MVtop_xcoord, MVtop_ycoord = get_coordinates("MVtop")

Pdist_xcoord, Pdist_ycoord = get_coordinates("Pdist")
Plat_xcoord, Plat_ycoord = get_coordinates("Plat")
Pmed_xcoord, Pmed_ycoord = get_coordinates("Pmed")
Prox_xcoord, Prox_ycoord = get_coordinates("Prox")

#%%

data = pd.concat([Cdist_xcoord, Cdist_ycoord, Cexten_xcoord, Cexten_ycoord, Clump_xcoord, Clump_ycoord, CslideTop_xcoord, CslideTop_ycoord,
                  Extensor_xcoord, Extensor_ycoord,
                  Latch_xcoord, Latch_ycoord,
                  MDist_xcoord, MDist_ycoord, MLat_xcoord, MLat_ycoord, MProx_xcoord, MProx_ycoord,
                  MVnotchP_xcoord, MVnotchP_ycoord, MVtip_xcoord, MVtip_ycoord, MVtop_xcoord, MVtop_ycoord,
                  Pdist_xcoord, Pdist_ycoord, Plat_xcoord, Plat_ycoord, Pmed_xcoord, Pmed_ycoord, Prox_xcoord, Prox_ycoord], axis=1)

data[data==0] = np.nan

data.loc[-3] = ['Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko',
                'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko',
                'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko', 'Hiko',
                'Hiko', 'Hiko']
data.loc[-2] = ['Cdist', 'Cdist', 'Cexten', 'Cexten', 'Clump', 'Clump', 'CslideTop', 'CslideTop',
                'Extensor', 'Extensor',
                'Latch', 'Latch',
                'MDist', 'MDist', 'MLat', 'MLat', 'MProx', 'MProx',
                'MVnotchP', 'MVnotchP', 'MVtip', 'MVtip', 'MVtop', 'MVtop',
                'Pdist', 'Pdist', 'Plat', 'Plat', 'Pmed', 'Pmed', 'Prox', 'Prox']
data.loc[-1] = ['x', 'y', 'x', 'y', 'x', 'y', 'x', 'y', 'x', 'y', 'x', 'y', 'x', 'y', 'x', 'y', 'x', 'y', 'x', 'y',
                'x', 'y', 'x', 'y', 'x', 'y', 'x', 'y', 'x', 'y', 'x', 'y']
data.index = data.index + 3
data = data.sort_index()

#new_col = ['scorer', 'bodyparts', 'coords']
new_col = [np.nan, np.nan, np.nan]
for i in range(0,10):
    new_col.append(file_name+"000"+str(i)+".png")
for j in range(10, len(MVtip_xcoord)):
    new_col.append(file_name+"00"+str(j)+".png")
    
new_col_2 = [np.nan, np.nan, np.nan]
for i in range(0, np.max([len(Cexten_xcoord),len(MVtip_xcoord)])):
    new_col_2.append(file_name)

new_col_3 = ['scorer', 'bodyparts', 'coords']
for i in range(0, len(MVtip_xcoord)):
    new_col_3.append('labeled-data')

data.insert(loc=0, column='new_col', value=new_col)
data.insert(loc=0, column='new_col_2', value=new_col_2)
data.insert(loc=0, column='new_col_3', value=new_col_3)
data.columns = range(data.columns.size)

data.to_csv(file_name+'.csv', index=False, header=False)

