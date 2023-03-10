import psycopg2

# Connect to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="com.1995"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Query the PostgreSQL server for a list of databases
cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
databases = cur.fetchall()

# Query the PostgreSQL server for a list of users
cur.execute("SELECT usename FROM pg_user;")
users = cur.fetchall()

# Print the list of databases
print("Databases:")
for database in databases:
    print(database[0])

# Print the list of users
print("\nUsers:")
for user in users:
    print(user[0])

# Close the cursor and the database connection
cur.close()
conn.close()
