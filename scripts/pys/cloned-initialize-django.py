import os
import re
import subprocess
import psycopg2
import time
import requests
import json
from pprint import pprint
from termcolor import colored
import shutil

print(colored("WARNING: This is a self-destructive script ❌. Proceed with caution!", "red"))
run_script = input("Are you sure you want to run the script? (Y/N) ")
if run_script.upper() != "Y":
    print("Script execution cancelled.")
else:
    venv_name = input("Do you want to create a virtual environment? (Y/N) ")
    if venv_name.upper() != "Y":
        print("No virtual environment created.")
    else:
        project_name = input("Enter the name of the project: ")
        venv_dir = "venv-" + project_name
        current_dir = os.getcwd()

        # Remove existing virtual environment directories
        for item in os.listdir(current_dir):
            if item.startswith("venv-"):
                item_path = os.path.join(current_dir, item)
                shutil.rmtree(item_path)

        # Create new virtual environment
        os.system(f"python3 -m venv {venv_dir}")

        # Print instructions for activating the virtual environment
        venv_path = os.path.join(current_dir, venv_dir)
        activate_path = os.path.join(venv_path, "bin/activate")
        print(colored(
            "To activate the virtual environment, run the following command:", "yellow"))
        print(f"source {activate_path}")


# -------CREATE POSTGRESQL DATABASE USER/PASSWORD/DATABASE
    want_database = input(colored("Do you want to create a database?", "cyan"))
    if want_database.upper() != "Y":
        print("No virtual environment created.")
    else:
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
            cursor.execute(
                f"CREATE USER {username} WITH PASSWORD '{password}'")

            # create the database and set the owner to the new user
            cursor.execute(f"CREATE DATABASE {dbname} OWNER {username}")

            cursor.close()
            conn.close()

        if __name__ == "__main__":
            print(colored("...Creating PostgreSQL USER/PASS/Database", "yellow"))
            time.sleep(3)
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            dbname = input("Enter the database name: ")
            create_user_and_database(username, password, dbname)
            print(colored("User and database created successfully!", "green"))
            time.sleep(3)

# -------REPLACING INSTANCES

    # Define the word you want to replace and the word you want to replace it with
    create_new_venv = input(
        "Do you want to replace an instances? (y/n): ")
    if create_new_venv.lower() not in ["yes", "y"]:
        print("Skipping the creation of a new virtual environment.")
        time.sleep(3)
    else:
        word = input("Enter the word: ")
        replace_with = input("Enter the new word to replace with old one: ")
        print("...replacing instances")
        time.sleep(3)
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
        print(colored("Instances replaced!", "green"))
        time.sleep(3)

# -------VERSION CONTROL

    print(colored("...Setting up GIT version control", "yellow"))
    time.sleep(3)

# -----------CREATING NEW ORIGIN END

# -----------ADD NEW ORIGIN START

# -------PUSHING CHANGES
    print(
        colored(f"...We're almost there {username} 🚀, hang on tightly", "green"))
    time.sleep(2)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "'initial commit'"])
    subprocess.run(["git", "push", "-u", "origin", "main"])
    print(colored("Changes pushed successfully", "green"))
    time.sleep(3)

    # --------NEW BACKUP BRANCH

    # Confirm completion
    pprint("initial script has been done ✅")
    time.sleep(3)
    print(colored("self destroying script ❌", "green"))
    time.sleep(4)
    # Remove the script
    # os.remove(__file__)
