import os
import re
import subprocess
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

# -----REPLACING INSTANCES

# Define the word you want to replace and the word you want to replace it with
word = input("Enter the word: ")
replace_with = input("Enter the new word to replace with old one: ")

# Search through all the Python files in your Django app
for root, dir, files in os.walk("/path/to/your/django/app"):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                content = f.read()

            # Replace all instances of the old word with the new word
            content = re.sub(word, replace_with, content)

            with open(file_path, "w") as f:
                f.write(content)

# ------DELETING OLD VIRTUAL ENVIRONMENT AND CREATING NEW_ONE

# Get the root directory of the current project
root_dir = os.getcwd()

# Prompt the user to confirm if they want to create a new virtual environment
create_new_venv = input(
    "Do you want to create a new virtual environment for this project? (y/n): ")
if create_new_venv.lower() not in ["yes", "y"]:
    print("Skipping the creation of a new virtual environment.")
else:
    # Prompt the user for the name of the new virtual environment
    new_venv_name = input(
        "Enter the name of the new virtual environment (without 'venv-' prefix): ")
    venv_name = "venv-" + new_venv_name

    # Delete the old virtual environment folder
    venv_path = os.path.join(root_dir, venv_name)
    if os.path.exists(venv_path):
        print(f"Deleting the old virtual environment: {venv_path}")
        subprocess.call(["rm", "-rf", venv_path])

    # Create a new virtual environment
    print(f"Creating a new virtual environment: {venv_path}")
    subprocess.call(["python3", "-m", "venv", venv_path])

    # Activate the virtual environment
    activate_script = os.path.join(venv_path, "bin", "activate")
    subprocess.call(["source", activate_script])

    # Install the dependencies from the requirements.txt file
    requirements_file = os.path.join(root_dir, "requirements.txt")
    subprocess.call(["pip", "install", "-r", requirements_file])
