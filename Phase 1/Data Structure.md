# Topic 2: Data Structures: The Organizers
Why It Matters: Raw data is useless without organization. These four structures are the primary ways you will store and manage collections of data, from a list of user IDs to the key-value properties of a single complex object.

# Core Concepts:

List: A mutable, ordered collection. Your go-to for a simple sequence of items.
Tuple: An immutable, ordered collection. Use it when data should not change (e.g., coordinates, RGB color values).
Dictionary (dict): The king of backend data structures. A collection of key-value pairs. Unordered (in older Python), but incredibly fast for lookups. This is how data like JSON is often represented.
Set: An unordered collection of unique items. Extremely fast for checking if an item exists in a collection.

## Code
```

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

```
# Your Mission:

Create a script student_grades.py.
Create a list of student names.
Create a dict where keys are student names (from your list) and values are their corresponding grades (e.g., 88, 92, 75).
Write code to calculate the average grade of all students.
Pick one student. Use an f-string to print their name and grade.
Create a set of all the subjects the students are taking (e.g., "Math", "Science"). Add a subject that's already there to prove that sets only store unique values.