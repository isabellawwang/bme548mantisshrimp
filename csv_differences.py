# import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%
Zanne = pd.read_csv('GE_122_071222_C1_090622_elastic_C001H001S0003pts_Zanne.csv')
Donovan = pd.read_csv('GE_122_071222_C1_090622_elastic_C001H001S0003pts_Donovan.csv')

Zanne = Zanne.apply(pd.to_numeric, errors='coerce')
Donovan = Donovan.apply(pd.to_numeric, errors='coerce')

Difference = Zanne.subtract(Donovan)

Difference = Difference.iloc[:, 3:]
Difference = Difference.iloc[2:, :]
Difference.index = Difference.index - 2
Difference = Difference.sort_index()

Difference.columns = ['Cdist_xcoord', 'Cdist_ycoord', 'Cexten_xcoord', 'Cexten_ycoord', 'Clump_xcoord', 'Clump_ycoord', 'CslideTop_xcoord', 'CslideTop_ycoord', 'Ctop_xcoord', 'Ctop_ycoord',
                  'Extensor_xcoord', 'Extensor_ycoord',
                  'Latch_xcoord', 'Latch_ycoord',
                  'MDist_xcoord', 'MDist_ycoord', 'MLat_xcoord', 'MLat_ycoord', 'MProx_xcoord', 'MProx_ycoord',
                  'MVBot_xcoord', 'MVBot_ycoord', 'MVnotchP_xcoord', 'MVnotchP_ycoord', 'MVtip_xcoord', 'MVtip_ycoord', 'MVtop_xcoord', 'MVtop_ycoord',
                  'Pdist_xcoord', 'Pdist_ycoord', 'Plat_xcoord', 'Plat_ycoord', 'Prox_xcoord', 'Prox_ycoord']

def find_dist(x, y):
    dist = (x**2+y**2)**0.5
    return dist

#%%
Dist_Diffs = []
Dist_Diffs_df = pd.DataFrame()

for i in range(0, Difference.shape[1], 2):
    col1 = Difference.iloc[:, i]
    col2 = Difference.iloc[:, i+1]
    col_dist = find_dist(col1, col2)
    Dist_Diffs.append(col_dist)

Dist_Diffs_df = pd.concat(Dist_Diffs, axis = 1)
    
Dist_Diffs_df.columns = ['Cdist', 'Cexten', 'Clump', 'CslideTop', 'Ctop',
                'Extensor',
                'Latch',
                'MDist', 'MLat', 'MProx',
                'MVBot', 'MVnotchP', 'MVtip', 'MVtop',
                'Pdist', 'Plat', 'Prox']

#%%
fig = plt.figure(num = 1, clear = True) #create figure
ax = fig.add_subplot(1,1,1) #create subplot
ax.grid(True)
ax.plot(Dist_Diffs_df, '.')
plt.xlabel('frame number') #x label
plt.ylabel('pixel difference') #y label
ax.legend(['Cdist', 'Cexten', 'Clump', 'CslideTop', 'Ctop',
                'Extensor',
                'Latch',
                'MDist', 'MLat', 'MProx',
                'MVBot', 'MVnotchP', 'MVtip', 'MVtop',
                'Pdist', 'Plat', 'Prox'],loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=4)
ax.set_ylim(0, 100)
fig.tight_layout() #tight layout
fig.savefig("Pix_diff.png", bbox_inches='tight', dpi=1000)
