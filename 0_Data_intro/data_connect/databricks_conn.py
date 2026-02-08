***
Databricks SQL Connector for Python
A native Python connector that allows running SQL statements on SQL warehouses. It converts between Databricks SQL and Python data types, removing the need for boilerplate code. Follow these steps to use the Python connector.
Step 1: Install the Databricks SQL Connector for Python library on your development machine by running
pip install databricks-sql-connector
Step 2: Create a personal access token to replace <access-token> in the code snippet below
Note
As a security best practice, you should not hard-code the personal access token into your code. Instead, you should retrieve this information from a secure location. For example, the code examples found in our documentation use environment variables.
Comment
What's this token for?
Serverless Starter Warehouse_PYTHON_CONNECT
Lifetime (days)
90
Step 3: Copy snippet below into your programming environment
Python
from databricks import sql
import os

connection = sql.connect(
                        server_hostname = "dbc-5b58b094-5bf8.cloud.databricks.com",
                        http_path = "/sql/1.0/warehouses/984c782006f448b7",
                        access_token = "<access-token>")

cursor = connection.cursor()

cursor.execute("SELECT * from range(10)")
print(cursor.fetchall())

cursor.close()
connection.close()
***