import psycopg2


def delete_user(username):
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="com.1995",
        database="postgres"
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # delete the user
    cursor.execute(f"DROP USER {username}")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    username = input("Enter the username to delete: ")
    delete_user(username)
    print(f"User {username} deleted successfully.")
