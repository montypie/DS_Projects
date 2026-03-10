import pandas as pd
from ydata_profiling import ProfileReport
# setuptools no longer being bundled with venvs from Python 3.12 -> pip install setuptools


#%%
# Simple example 
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Basic profiling report
profile = ProfileReport(df, title="Titanic Analysis")
profile.to_file("titanic_report.html")
print("Report saved as titanic_report.html")