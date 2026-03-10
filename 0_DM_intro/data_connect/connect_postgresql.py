#%%
import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd


#%%

#%%
def load_database_data(query="SELECT * FROM spelers;"):
    """ Load custom query from POSTGRESQL database and return as a DataFrame. 
    
    Parameters:
    query (str): SQL query to execute. Default is 'SELECT * FROM spelers'.

    Returns:
    pd.DataFrame: DataFrame containing the query results.
    """

    # Load environment variables from .env
    load_dotenv()

    # Fetch variables
    USER = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")
    HOST = os.getenv("HOST")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")
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
        
        the_data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        the_df = pd.DataFrame(the_data, columns=columns)


        # Close the cursor and connection
        cursor.close()
        connection.close()
        print("Connection closed.")
        return the_df

    except Exception as e:
        print(f"Failed to connect: {e}")
        return None