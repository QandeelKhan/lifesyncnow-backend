import psycopg2

# Connect to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="com.1995"
)

# Set autocommit to True
conn.autocommit = True

# Open a cursor to perform database operations
cur = conn.cursor()

# Retrieve the list of all databases
cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
rows = cur.fetchall()
db_list = [row[0] for row in rows]

# Display the list of databases to the user
print("Available databases:")
for db_name in db_list:
    print(db_name)

# Prompt the user to enter the name of the database to drop
db_name = input("Enter the name of the database to drop: ")

# Check if the database exists
if db_name in db_list:
    # Drop the database
    cur.execute(f"DROP DATABASE {db_name};")
    print(f"The database {db_name} has been dropped.")
else:
    print(f"The database {db_name} does not exist.")

cur.close()
conn.close()
