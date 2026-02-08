#%%
import duckdb
import pandas as pd

# Create a DuckDB connection
conn = duckdb.connect()

# Query the CSV file to count the number of rows
result = conn.execute("SELECT COUNT(*) FROM 'data/itineraries.csv'").fetchone()

print(f"Number of rows in itineraries.csv: {result[0]}")
#%%
# Query to get the top 5 rows and convert to DataFrame
df = conn.execute("SELECT * FROM 'data/itineraries.csv' LIMIT 5").df()

# Display the DataFrame
print("Top 5 rows from itineraries.csv:")
print(df)
# Close the connection
conn.close()


# With pandas
#%%
import pandas as pd

# WARNING: This will load all 82+ million rows into memory!
df = pd.read_csv('data/itineraries.csv')
row_count = len(df)
print(f"Total number of rows: {row_count}")

#%%
# Read the CSV file and get the top 5 rows
df_top5 = pd.read_csv('data/itineraries.csv', nrows=5)

# Display the top 5 rows
print("Top 5 rows from itineraries.csv using pandas:")
print(df_top5)