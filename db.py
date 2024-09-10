import os
import json

class PotatoDB:

    def __init__(self, folder="LazyDB"):
        self.tables = {}
        self.set_folder(folder)
        self.load()

    def create_table(self, table_name):
        """Creates a new table."""
        self.tables[table_name] = []
        self.save(table_name)

    def insert(self, table_name, data):
        """Inserts a new record into the specified table."""
        if table_name in self.tables:
            self.tables[table_name].append(data)
        else:
            # If table does not exist, create it and insert data
            self.tables[table_name] = [data]
        self.save(table_name)
        return data
    
    def query(self, table_name, query_func):
        """Queries data from the specified table using a query function."""
        if table_name in self.tables:
            result = list(filter(query_func, self.tables[table_name]))
            return result
        else:
            return None

    def update(self, table_name, condition_func, update_func):
        """Updates records in the specified table based on a condition."""
        if table_name in self.tables:
            for record in self.tables[table_name]:
                if condition_func(record):
                    update_func(record)
            self.save(table_name)
            return True
        else:
            return False

    def delete(self, table_name, condition_func):
        """Deletes records from the specified table based on a condition."""
        if table_name in self.tables:
            self.tables[table_name] = [record for record in self.tables[table_name] if not condition_func(record)]
            self.save(table_name)
            return True
        else:
            return False

    def set_folder(self, folder_name):
        """Sets the folder where the tables will be saved and loaded."""
        self.folder = folder_name
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        return True

    def save(self, table_name=None):
        """Saves the specified table to a JSON file in the set folder, using the table name as the filename."""
        if table_name:
            if table_name in self.tables:
                filename = os.path.join(self.folder, f"{table_name}.json")
                with open(filename, 'w') as file:
                    json.dump(self.tables[table_name], file, indent=4)
            else:
                raise ValueError(f"Table '{table_name}' does not exist.")
        else:
            # Save all tables to the folder
            for table_name in self.tables:
                filename = os.path.join(self.folder, f"{table_name}.json")
                with open(filename, 'w') as file:
                    json.dump(self.tables[table_name], file, indent=4)

    def load(self, table_name=None):
        """Loads a table from a JSON file in the set folder. If table_name is not specified, it loads all tables."""
        if self.folder:
            if table_name:
                filename = os.path.join(self.folder, f"{table_name}.json")
                if os.path.exists(filename):
                    with open(filename, 'r') as file:
                        self.tables[table_name] = json.load(file)
                    return True
                else:
                    raise ValueError(f"Table '{table_name}' does not exist.")
            else:
                # Load all tables from the folder
                for file in os.listdir(self.folder):
                    if file.endswith('.json'):
                        table_name = os.path.splitext(file)[0]
                        with open(os.path.join(self.folder, file), 'r') as json_file:
                            self.tables[table_name] = json.load(json_file)
        else:
            raise ValueError("Folder not set. Use set_folder method to set the folder path.")
