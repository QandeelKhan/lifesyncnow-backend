import os
import sys
from django.core.management import execute_from_command_line
from django.core.management.commands import flush


# Prompt the user for the app name
app_name = input("Enter the name of the Django app to flush data from: ")

# Call the flush command with the appropriate options
options = {
    "interactive": False,
    "database": "default",
    "app_name": app_name,
    "verbosity": 1,
    "no_color": False,
    "skip_checks": False,
}
execute_from_command_line(["manage.py", "flush"], options=options)
