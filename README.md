# PotatoDB: Lightweight JSON-based Database for Python

![PotatoDB Cover](https://github.com/Kawai-Senpai/PotatoDB/blob/81f8b44b0718fcd396a296933eb72bc1e35e3053/Assets/PotatoDB%20Thumbnail.png)

**PotatoDB** is a lightweight, JSON-based database solution designed for simplicity and ease of use. It allows you to create, insert, query, update, and delete records in a NoSQL fashion, using Python's built-in JSON module to store data persistently on disk developed by [*Ranit Bhowmick*](https://www.linkedin.com/in/ranitbhowmick/) & [*Sayanti Chatterjee*](https://www.linkedin.com/in/sayantichatterjee/). Whether you need a quick and easy database for small projects, prototypes, or educational purposes, PotatoDB offers a flexible solution without the overhead of traditional databases.

## Features

- **Simple Setup:** No need for external dependencies or database servers. PotatoDB works out of the box with Python's standard library.
- **JSON-based Storage:** Data is stored in human-readable JSON files, making it easy to inspect and manipulate outside of the application.
- **In-Memory Operations:** Perform operations like querying, updating, and deleting records in memory for fast performance.
- **Automatic Persistence:** Data is automatically saved to disk after each operation, ensuring data integrity.
- **Table-based Structure:** Create multiple tables within a single database instance.
- **Dynamic Schema:** No predefined schema; records can have varying fields, offering flexibility for evolving data models.

## Table of Contents

1. [Installation](#installation)
2. [Basic Usage](#basic-usage)
    - [Creating a Database Instance](#creating-a-database-instance)
    - [Creating a Table](#creating-a-table)
    - [Inserting Records](#inserting-records)
    - [Querying Records](#querying-records)
    - [Updating Records](#updating-records)
    - [Deleting Records](#deleting-records)
3. [Detailed Documentation](#detailed-documentation)
    - [Class: `PotatoDB`](#class-PotatoDB)
    - [Methods](#methods)
        - [`__init__`](#init)
        - [`create_table`](#create_table)
        - [`insert`](#insert)
        - [`query`](#query)
        - [`update`](#update)
        - [`delete`](#delete)
        - [`set_folder`](#set_folder)
        - [`save`](#save)
        - [`load`](#load)
4. [Examples](#examples)
5. [Advanced Usage](#advanced-usage)
6. [Limitations](#limitations)
7. [Future Enhancements](#future-enhancements)
8. [Contributing](#contributing)

## Installation

PotatoDB is implemented in pure Python and does not require any external dependencies. To start using PotatoDB, simply download the source code and include it in your project or install it via pip.

```bash
pip install potatodb
```

Alternatively, you can copy the `potatodb.py` file directly into your project directory.

## Basic Usage

### Creating a Database Instance

To create a new instance of PotatoDB, import the `PotatoDB` class and specify the folder where the data should be stored. If the folder does not exist, it will be created automatically.

```python
from potatodb.db import PotatoDB

# Create a new PotatoDB instance
db = PotatoDB("example_data")
```

### Creating a Table

To create a new table within the database, use the `create_table` method.

```python
db.create_table("users")
```

### Inserting Records

Records can be inserted into a table using the `insert` method. The record should be a Python dictionary.

```python
db.insert("users", {"name": "Alice", "age": 30})
db.insert("users", {"name": "Bob", "age": 25}) 
# The database will automatically save the data to disk after each operation
```

### Querying Records

To query records, use the `query` method with a custom query function. The query function should return `True` for records that match the condition and `False` for those that don't.

```python
# Query all users
all_users = db.query("users", lambda record: True)
print("All users:", all_users)

# Query users older than 30
users_above_30 = db.query("users", lambda record: record["age"] > 30)
print("Users above 30:", users_above_30)
```

### Updating Records

To update records, use the `update` method with a condition function and an update function.

```python
# Update the age of all users named "Alice" to 35
db.update("users", lambda record: record["name"] == "Alice", lambda record: record.update({"age": 35}))
```

### Deleting Records

To delete records, use the `delete` method with a condition function.

```python
# Delete all users named "Bob"
db.delete("users", lambda record: record["name"] == "Bob")
```

## Detailed Documentation

### Class: `PotatoDB`

The `PotatoDB` class is the core of the PotatoDB library. It provides methods for creating tables, inserting data, querying, updating, and deleting records, as well as saving and loading data to and from JSON files.

#### `__init__`

```python
def __init__(self, folder="PotatoDB"):
```

- **Description:** Initializes the database instance, setting the folder for storage and loading existing data from JSON files.
- **Parameters:**
  - `folder` (str): The folder where the database files will be stored. Defaults to `"PotatoDB"`.

#### `create_table`

```python
def create_table(self, table_name):
```

- **Description:** Creates a new table within the database.
- **Parameters:**
  - `table_name` (str): The name of the table to be created.

#### `insert`

```python
def insert(self, table_name, data):
```

- **Description:** Inserts a new record into the specified table.
- **Parameters:**
  - `table_name` (str): The name of the table where the record will be inserted.
  - `data` (dict): The record to be inserted, represented as a dictionary.
- **Returns:** The inserted record.

#### `query`

```python
def query(self, table_name, query_func):
```

- **Description:** Queries data from the specified table using a query function.
- **Parameters:**
  - `table_name` (str): The name of the table to query.
  - `query_func` (function): A function that takes a record as input and returns `True` if the record matches the query, `False` otherwise.
- **Returns:** A list of records that match the query.

#### `update`

```python
def update(self, table_name, condition_func, update_func):
```

- **Description:** Updates records in the specified table based on a condition.
- **Parameters:**
  - `table_name` (str): The name of the table to update.
  - `condition_func` (function): A function that takes a record as input and returns `True` if the record should be updated.
  - `update_func` (function): A function that takes a record as input and performs the update.
- **Returns:** `True` if the update was successful, `False` otherwise.

#### `delete`

```python
def delete(self, table_name, condition_func):
```

- **Description:** Deletes records from the specified table based on a condition.
- **Parameters:**
  - `table_name` (str): The name of the table from which records should be deleted.
  - `condition_func` (function): A function that takes a record as input and returns `True` if the record should be deleted.
- **Returns:** `True` if the deletion was successful, `False` otherwise.

#### `set_folder`

```python
def set_folder(self, folder_name):
```

- **Description:** Sets the folder where the tables will be saved and loaded.
- **Parameters:**
  - `folder_name` (str): The name of the folder.

#### `save`

```python
def save(self, table_name=None):
```

- **Description:** Saves the specified table to a JSON file in the set folder. (This method is called automatically after each operation.)
- **Parameters:**
  - `table_name` (str): The name of the table to save. If `None`, all tables are saved.

#### `load`

```python
def load(self, table_name=None):
```

- **Description:** Loads a table from a JSON file in the set folder. (This method is called automatically when the database is initialized.)
- **Parameters:**
  - `table_name` (str): The name of the table to load. If `None`, all tables are loaded.

## Examples

Here's a complete example of how to use PotatoDB:

```python
from potatodb.db import PotatoDB

# Create a new LazyDB instance
db = PotatoDB("example_data")

# Create a new table called "users"
db.create_table("users")

# Insert a new record into the "users" table
db.insert("users", {"name": "Alice", "age": 30})
db.insert("users", {"name": "Bob", "age": 25})

# Query all records from the "users" table
all_users = db.query("users", lambda record: True)
print("All users:" , all_users)

# Update the age of all users named "Alice" to 35
db.update("users", lambda record: record["name"] == "Alice", lambda record: record.update({"age": 35}))

# Query all records above the age of 30 from the "users" table
users_above_30 = db.query("users", lambda record: record["age"] > 30)

# Print the updated records
print("Users above 30:", users_above_30)

# Delete all users named "Bob" from the "users" table
db.delete("users", lambda record: record["name"] == "Bob")

# Query all records from the "users" table after deletion
remaining_users = db.query("users", lambda record: True)

# Print the remaining records
print("Remaining users:", remaining_users)
```

## Advanced Usage

### Custom Data Persistence

While PotatoDB automatically saves and loads data from JSON files, you can also manually save or load data using custom file paths or formats. This allows you to integrate PotatoDB with other data management systems or customize the storage format.

## Limitations

- **Performance:** PotatoDB is designed for lightweight tasks and may not perform well with large datasets or complex queries.
- **Concurrency:** PotatoDB is not thread-safe and should be used with caution in multi-threaded environments.
- **Data Integrity:** Since PotatoDB writes data to JSON files, there is a risk of data corruption if the program crashes during a write operation.

## Future Enhancements

- **Indexing:** Implementing indexing for faster query performance.
- **Transactions:** Adding support for transactions to ensure data integrity during complex operations.
- **Data Export/Import:** Adding features to export and import data in different formats, such as CSV or XML.

## Contributing

Contributions are welcome! If you find a bug or want to suggest a feature, feel free to open an issue or submit a pull request on GitHub.
