import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd
from ydata_profiling import ProfileReport

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

#%%
def load_database_data(query="SELECT * FROM TENNIS.SPELERS;"):
    """ Connect to db en load spelers db """

    # Connect to the database
    try:
        connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )
        print("Connection successful!")

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()
        
        # Example query
        # cursor.execute("SELECT NOW();")
        # result = cursor.fetchone()
        # print("Current Time:", result)
        
        cursor.execute(query)

        fetched_data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data_df = pd.DataFrame(fetched_data, columns=columns)

        # Close the cursor and connection
        cursor.close()
        connection.close()
        print("Connection closed.")
        return data_df

    except Exception as e:
        print(f"Failed to connect: {e}")