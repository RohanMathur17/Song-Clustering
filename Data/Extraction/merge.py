import pandas as pd
import numpy as np

np.random.seed(10)

country     = pd.read_csv(r'C:\Users\ROSHAN\Documents\GitHub\Song-Clustering\Data\Country.csv')
death_metal = pd.read_csv(r'C:\Users\ROSHAN\Documents\GitHub\Song-Clustering\Data\Death-Metal.csv')
lofi        = pd.read_csv(r'C:\Users\ROSHAN\Documents\GitHub\Song-Clustering\Data\Lo-Fi.csv')


#Removing random rows from each dataset to get equal amount of rows for each
remove_n = 69
drop_indices = np.random.choice(country.index, remove_n, replace=False)
country_subset = country.drop(drop_indices)
country_subset['Cluster'] = 0 

remove_n = 8 
drop_indices = np.random.choice(death_metal.index, remove_n, replace=False)
death_metal_subset = death_metal.drop(drop_indices)
death_metal_subset['Cluster'] = 1

remove_n = 4
drop_indices = np.random.choice(lofi.index, remove_n, replace=False)
lofi_subset = lofi.drop(drop_indices)
lofi_subset['Cluster'] = 2

merged = [country_subset,death_metal_subset, lofi_subset]

merged_df = pd.concat(merged,ignore_index= True)  #Merging the subsets

merged_df.to_csv('Dataset.csv' , index = False) #Creating a csv