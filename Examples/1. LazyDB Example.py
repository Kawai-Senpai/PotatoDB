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
