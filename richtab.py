import json
from rich.console import Console
from rich.table import Table

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def display_table(data):
    table = Table(title="JSON Data")

    # Add columns
    for key in data[0].keys():
        table.add_column(key)

    # Add rows
    for item in data:
        table.add_row(*[str(value) for value in item.values()])

    console = Console()
    console.print(table)

if __name__ == "__main__":
    file_path = 'testdata.json'
    data = read_json(file_path)
    display_table(data)