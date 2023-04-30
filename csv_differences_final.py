# import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the list of all files and directories
path = "/home/col/Desktop/BME548/HikoIsabella/ResultCSVs"
dir_list = os.listdir(path)
dir_list = sorted(dir_list)
dir_list = ["/home/col/Desktop/BME548/HikoIsabella/ResultCSVs/" + s for s in dir_list]

all_column_diffs = []
count = 0

for i in range(0,48,2):
    manual = pd.read_csv(dir_list[i])
    model = pd.read_csv(dir_list[i+1])

    to_remove = np.arange(0, model.columns.size, 3)
    model = model.drop(model.columns[to_remove], axis=1)

    manual = manual.drop(manual.columns[[0,1,2]], axis=1)

    manual = manual.apply(pd.to_numeric, errors='coerce')
    model = model.apply(pd.to_numeric, errors='coerce')
    model.columns = manual.columns


    Difference = manual.subtract(model)

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
    all_column_diffs.append(column_diffs)
    count += 1

averages = np.average(all_column_diffs, axis=0)
fig = plt.figure(num = 1, clear = True) #create figure
ax = fig.add_subplot(1,1,1) #create subplot
ax.grid(color='gray', linestyle='dotted', linewidth=1)
ax.bar(column_diffs.index, averages)
plt.xlabel('Location') #x label
plt.ylabel('Pixel Difference') #y label
plt.title("Average Pixel Difference in Test Set")
ax.set_xticklabels(ax.get_xticklabels(), rotation = 45)
fig.tight_layout() #tight layout
fig.savefig("/home/col/Desktop/BME548/HikoIsabella/Testing/Pix_diff2.png", bbox_inches='tight', dpi=1000)
print(count)
print(all_column_diffs)
print(np.average(all_column_diffs, axis=0))
