# utils/csv.py
class util_csv:
    @staticmethod
    def dictReaderFirstRow(path):
        # Mock implementation for reading the first row of a CSV file
        # This should be replaced with the actual code from utils/csv.py
        return {"tk_game_name": "Sample Game"}  # Example data

# add-category.py
def add_category():
    display_output("Category added")

# add-run.py
def add_run():
    display_output("Run added")

# generate.py
def generate_report():
    display_output("Report generated")

# setup.py
def setup_environment():
    display_output("Environment set up")

# Main helper script (paceboard.py combined with others)
import os
from js import document
from pyodide.ffi import create_proxy

def generate():
    """Regenerate site"""
    display_output("Regenerating site...")
    runIdName = "tk_run_id"
    categoryIdName = "tk_category_dashname"
    config = util_csv.dictReaderFirstRow("csv/config.csv")
    if len(config) != 0:
        generate_report()

def optionSetup():
    """Reconfigure site details"""
    display_output("Running setup...")
    setup_environment()
    generate()

def optionAddCategory():
    """Add category"""
    display_output("Adding category...")
    add_category()
    generate()

def optionAddRun():
    """Add run"""
    display_output("Adding run...")
    add_run()
    generate()

def optionQuit():
    """Quit"""
    display_output("Quitting...")
    os._exit(1)

def display_output(message):
    output_element = document.getElementById("output")
    output_element.innerHTML += f"<p>{message}</p>"

# If no setup completed, run setup script
config = util_csv.dictReaderFirstRow("csv/config.csv")
if len(config) == 0:
    display_output("No setup found. Running setup...")
    optionSetup()

# Set options (functions as defined earlier)
options = [optionSetup, optionAddCategory, optionAddRun, optionQuit]

def display_options():
    key = "tk_game_name"
    config = util_csv.dictReaderFirstRow("csv/config.csv")
    display_output(f"\n[ paceboard for {config[key]} ]")
    for index, option in enumerate(options):
        display_output(f"{index + 1} - {option.__doc__}")

display_options()

def submitChoice(event=None):
    display_output("Submit button clicked")  # Debugging statement
    try:
        rawOptionInput = document.getElementById("userInput").value
        display_output(f"User input: {rawOptionInput}")  # Debugging statement
        optionInput = int(rawOptionInput)
        if 0 < optionInput <= len(options):
            display_output(f"Executing option {optionInput}...")  # Debugging statement
            options[optionInput - 1]()
        else:
            display_output("Not a valid choice!")
    except ValueError:
        display_output("Not a valid choice! Please enter a number.")
    except KeyboardInterrupt:
        display_output("\nProcess interrupted. Exiting...")
        os._exit(1)

# Bind the submitChoice function to the button click using create_proxy
submit_button = document.getElementById("submitButton")
submit_button.addEventListener("click", create_proxy(submitChoice))

input_element = document.getElementById("userInput")
input_element.addEventListener("keydown", create_proxy(lambda event: submitChoice() if event.key == "Enter" else None))
input_element.focus()
