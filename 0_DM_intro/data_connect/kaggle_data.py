#%% imports
import os
import kagglehub
#import pandas as pd
#import dtale

#%% Download dataset
os.environ['KAGGLEHUB_CACHE'] = 'C:/DataScienceCourse/DataScience_Les1'
path = kagglehub.dataset_download("dilwong/flightprices")

#%% Exploring data
#Titanic_df = pd.read_csv(f"{path}/Titanic-Dataset.csv")
#Titanic_df.info()

#d = dtale.show(Titanic_df)
#d.open_browser()
print(f"Dataset downloaded successfully.")