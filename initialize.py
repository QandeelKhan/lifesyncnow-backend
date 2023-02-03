import psycopg2


def create_user_and_database(username, password, dbname):
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="com.1995",
        database="postgres"
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # create the user
    cursor.execute(f"CREATE USER {username} WITH PASSWORD '{password}'")

    # create the database and set the owner to the new user
    cursor.execute(f"CREATE DATABASE {dbname} OWNER {username}")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    dbname = input("Enter the database name: ")
    create_user_and_database(username, password, dbname)
    print("User and database created successfully.")
