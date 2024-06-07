# utils/csv.py
class util_csv:
    @staticmethod
    def dictReaderFirstRow(path):
        # Mock implementation for reading the first row of a CSV file
        # This should be replaced with the actual code from utils/csv.py
        return {"tk_game_name": "Sample Game"}  # Example data

# add-category.py
def add_category():
    print("Category added")

# add-run.py
def add_run():
    print("Run added")

# generate.py
def generate_report():
    print("Report generated")

# setup.py
def setup_environment():
    print("Environment set up")

# Main helper script (paceboard.py combined with others)
import os

def generate():
    """Regenerate site"""
    runIdName = "tk_run_id"
    categoryIdName = "tk_category_dashname"
    config = util_csv.dictReaderFirstRow("csv/config.csv")
    if len(config) != 0:
        generate_report()

def optionSetup():
    """Reconfigure site details"""
    setup_environment()
    generate()

def optionAddCategory():
    """Add category"""
    add_category()
    generate()

def optionAddRun():
    """Add run"""
    add_run()
    generate()

def optionQuit():
    """Quit"""
    print()
    os._exit(1)

# If no setup completed, run setup script
config = util_csv.dictReaderFirstRow("csv/config.csv")
if len(config) == 0:
    optionSetup()

# Set options (functions as defined earlier)
options = [optionSetup, optionAddCategory, optionAddRun, optionQuit]

# Main loop and input handler
while True:
    key = "tk_game_name"
    config = util_csv.dictReaderFirstRow("csv/config.csv")
    print(f"\n[ paceboard for {config[key]} ]")
    for index, option in enumerate(options):
        print(f"{index + 1} - {option.__doc__}")
    try:
        rawOptionInput = input("Your pick:  ")
        optionInput = int(rawOptionInput)
        if 0 < optionInput <= len(options):
            options[optionInput - 1]()
        else:
            print("Not a valid choice!")
    except ValueError:
        print("Not a valid choice!")
    except KeyboardInterrupt:
        os._exit(1)
