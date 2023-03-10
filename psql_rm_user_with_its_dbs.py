import psycopg2
from psycopg2.extensions import AsIs

# Connect to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="com.1995"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Prompt the user for the name of the user to delete
username = input("Enter the username to delete: ")

# Check if the user exists
cur.execute("""
    SELECT 1 FROM pg_user u
    LEFT JOIN pg_database d ON u.usename = d.datname
    WHERE u.usename = %s OR d.datname = %s;
""", (username, username))

if cur.fetchone():
    # Drop the user and all of its related databases
    cur.execute("DROP OWNED BY %s CASCADE;", (AsIs(username),))
    cur.execute("DROP USER %s;", (AsIs(username),))
    conn.commit()
    print(f"The user {username} and its related databases have been dropped.")
else:
    print(f"The user {username} does not exist.")

cur.close()
conn.close()
