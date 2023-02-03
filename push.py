import subprocess
subprocess.run(["pip", "freeze", ">", "requirements.txt"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "auto commit by py script"])
subprocess.run(["git", "push"])
