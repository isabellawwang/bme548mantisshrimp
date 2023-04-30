# import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

manual = pd.read_csv('/home/col/Desktop/BME548/HikoIsabella/ResultCSVs/GE_104_071222_C1_091222_elastic_C001H001S0014.csv')
model = pd.read_csv('/home/col/Desktop/BME548/HikoIsabella/ResultCSVs/GE_104_071222_C1_091222_elastic_C001H001S0014DLC_resnet50_shrimp_final_5Apr30shuffle1_1000.csv')

to_remove = np.arange(0, model.columns.size, 3)
model = model.drop(model.columns[to_remove], axis=1)

manual = manual.drop(manual.columns[[0,1,2]], axis=1)

manual = manual.apply(pd.to_numeric, errors='coerce')
model = model.apply(pd.to_numeric, errors='coerce')
model.columns = manual.columns


Difference = manual.subtract(model)

#Difference = Difference.iloc[:, 3:]
#Difference = Difference.iloc[2:, :]
Difference.index = Difference.index - 2
Difference = Difference.sort_index()

print(Difference)
Difference.columns = ['Cdist_xcoord', 'Cdist_ycoord', 'Cexten_xcoord', 'Cexten_ycoord', 'Clump_xcoord', 'Clump_ycoord', 'CslideTop_xcoord', 'CslideTop_ycoord', 'Ctop_xcoord', 'Ctop_ycoord',
                  'Extensor_xcoord', 'Extensor_ycoord',
                  'Latch_xcoord', 'Latch_ycoord',
                  'MDist_xcoord', 'MDist_ycoord', 'MLat_xcoord', 'MLat_ycoord', 'MProx_xcoord', 'MProx_ycoord',
                  'MVBot_xcoord', 'MVBot_ycoord', 'MVnotchP_xcoord', 'MVnotchP_ycoord', 'MVtip_xcoord', 'MVtip_ycoord', 'MVtop_xcoord', 'MVtop_ycoord',
                  'Pdist_xcoord', 'Pdist_ycoord', 'Plat_xcoord', 'Plat_ycoord', 'Prox_xcoord', 'Prox_ycoord']

def find_dist(x, y):
    dist = (x**2+y**2)**0.5
    return dist

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

column_diffs = Dist_Diffs_df.mean(axis=0)

fig = plt.figure(num = 1, clear = True) #create figure
ax = fig.add_subplot(1,1,1) #create subplot
ax.grid(True)
ax.plot(Dist_Diffs_df, '.')
plt.xlabel('Frame Number') #x label
plt.ylabel('Pixel Difference') #y label
plt.title('Pixel Difference by Frame for Test Video #2')
ax.legend(['Cdist', 'Cexten', 'Clump', 'CslideTop', 'Ctop',
                'Extensor',
                'Latch',
                'MDist', 'MLat', 'MProx',
                'MVBot', 'MVnotchP', 'MVtip', 'MVtop',
                'Pdist', 'Plat', 'Prox'],loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=4)
ax.set_ylim(0, 200)
fig.tight_layout() #tight layout
fig.savefig("/home/col/Desktop/BME548/HikoIsabella/Testing/Pix_diff.png", bbox_inches='tight', dpi=1000)
