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

def optionAddCategory():
    """Add category"""
    add_category()

def
