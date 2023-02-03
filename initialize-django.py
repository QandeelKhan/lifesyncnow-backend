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
        print(colored("To activate the virtual environment, run the following command:", "yellow"))
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
            cursor.execute(f"CREATE USER {username} WITH PASSWORD '{password}'")

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
    username = os.environ["GH_USERNAME"]
    token = os.environ["GH_TOKEN"]
    email = os.environ["GH_EMAIL"]
    api_base_url = "https://api.github.com"
# -----------CREATING NEW ORIGIN

    # Prompt the user for the repository name
    repo_name = input("Enter the name of the repository you want to create: ")

    # Define the API endpoint for getting the user's repositories
    repos_endpoint = f"{api_base_url}/user/repos"

    # Set up authentication headers
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Make the API request to get the user's repositories
    response = requests.get(repos_endpoint, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # Get the list of repositories
        repos = response.json()

        # Check if the repository already exists
        repo_exists = False
        for repo in repos:
            if repo["name"] == repo_name:
                repo_exists = True
                break

    # If the repository already exists, prompt the user to enter a new name
    if repo_exists:
        print(f"Repository with the name '{repo_name}' already exists.")
        repo_name = input("Please enter a new name for the repository: ")

    # Prompt the user for the repository description
    repo_description = input(
        "Please enter the description of the repository you want to create: ")

    # Define the API endpoint for creating the repository
    create_repo_endpoint = f"{api_base_url}/user/repos"

    # Define the request data
    data = {
        "name": repo_name,
        "description": repo_description,
        "private": False
    }

    # Make the API request to create the repository
    response = requests.post(create_repo_endpoint, headers=headers, json=data)

    # Check the response status code
    if response.status_code == 201:
        print(f"Successfully created repository: {repo_name}")
        repo_origin = f"https://github.com/{username}/{repo_name}"
        print(f"Repository origin address: {repo_origin}")
        time.sleep(2)
    else:
        print(f"Failed to create repository: {repo_name}")
        print(f"Response status code: {response.status_code}")
        try:
            response_json = response.json()
            print(f"Response message: {response_json['message']}")
        except:
            print(f"Response: {response.text}")

# -----------CREATING NEW ORIGIN END

# -----------ADD NEW ORIGIN START
    # Ask for new origin
    # origin_url = input("Enter the new origin URL: ")

    # Add the new origin
    subprocess.run(["git", "remote", "add", "origin", repo_origin])
    print(colored("new repository origin added successfully!", "green"))
    time.sleep(2)


# -------ADDING COLLABORATOR

    # Prompt the user to confirm if they have collaborators to add
    collaborator_username = None
    add_collaborators = input(
        "Do you have any collaborators to add? (yes/no): ").lower()

    # Add each collaborator
    while add_collaborators in ["yes", "y"]:
        # Prompt the user for the collaborator username
        collaborator_username = input(
            "Enter the username of the collaborator: ")

        # Define the API endpoint
        endpoint = f"{api_base_url}/repos/{username}/{repo_name}/collaborators/{collaborator_username}"

        # Make the API request to add the collaborator
        response = requests.put(endpoint, headers=headers)

        # Check the response status code
        # if response.status_code == 204:
        if response.status_code == 201:
            print(f"Successfully added collaborator: {collaborator_username}")
            time.sleep(3)
        else:
            print(f"Failed to add collaborator: {collaborator_username}")
            print(f"Response: {response.text}")
            time.sleep(2)

        # Prompt the user to confirm if they have another collaborator to add
        add_collaborators = input(
            "Do you have another collaborator to add? (yes/no): ").lower()

    if add_collaborators in ["no", "n"] and collaborator_username is not None:
        print(f"No more collaborators added other then {collaborator_username}.")
# -------ADDING COLLABORATOR END

# -------PUSHING CHANGES
    print(
        colored(f"...We're almost there {username} 🚀, hang on tightly", "green"))
    time.sleep(3)
    print(
        colored(f"...pushing changes to newly added repository: {repo_origin}", "cyan"))
    time.sleep(2)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "'initial commit'"])
    subprocess.run(["git", "push", "-u", "origin", "main"])
    print(colored("Changes pushed successfully", "green"))
    time.sleep(3)


# --------NEW BACKUP BRANCH
    # Replace <OWNER> and <REPO> with your GitHub repository information
    # The API endpoint to get the latest commit sha for an existing branch
    url = f"https://api.github.com/repos/{username}/{repo_name}/git/refs/heads/main"

    # Make a GET request to retrieve the latest commit sha for the branch
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        latest_commit_sha = response.json()["object"]["sha"]
    else:
        print(
            f"Failed to retrieve latest commit sha: {response.json()['message']}")
        exit()

    # The API endpoint to create a new branch
    url = f"https://api.github.com/repos/{username}/{repo_name}/git/refs"

    # Define the branch name and the latest commit sha
    data = {
        "ref": "refs/heads/backup-branch",
        "sha": latest_commit_sha
    }

    # Make a POST request to create the new branch
    response = requests.post(url, json=data, headers=headers)

    # Check if the request was successful
    if response.status_code == 201:
        print("Branch created successfully")
    else:
        print(f"Failed to create branch: {response.json()['message']}")

    # --------NEW BACKUP BRANCH

    # Confirm completion
    pprint("initial script has been done ✅")
    time.sleep(3)
    print(colored("self destroying script ❌", "green"))
    time.sleep(4)
    # Remove the script
    # os.remove(__file__)
