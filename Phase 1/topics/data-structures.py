
# List: A list of tasks for a user. Mutable.
tasks = ["Buy groceries", "Pay bills", "Walk the dog"]
tasks.append("Code for an hour") # Add an item
tasks.remove("Pay bills")     # Remove an item
print(f"Today's tasks: {tasks}")
print(f"First task: {tasks[0]}") # Access by index

# Tuple: A set of coordinates. Immutable.
database_host_port = ("db.example.com", 5432)
# database_host_port[0] = "new.db.com" # This would raise a TypeError!

# Dictionary: A single user object. The workhorse of APIs.
user_profile = {
    "user_id": 101,
    "username": "alex",
    "email": "alex@example.com",
    "is_premium": False
}
print(f"User's email: {user_profile['email']}") # Access by key
user_profile["is_premium"] = True # Update a value

# Set: A collection of unique tags for a blog post.
tags = {"python", "django", "backend", "python"} # Duplicate "python" is ignored
print(f"Tags: {tags}")
print(f"Does the post have a 'django' tag? {'django' in tags}") # Fast check