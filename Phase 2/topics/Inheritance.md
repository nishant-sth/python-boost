## Topic 2: Inheritance (Building on Shoulders of Giants)
Why It Matters: Inheritance is a cornerstone of code reuse. Instead of writing the same code over and over, you create a base class with common functionality and then have specialized classes inherit from it. When you write class Post(models.Model): in Django, you are inheriting all the powerful database features from Django's Model class for free.

# Core Concepts:

Parent/Base Class: The class that is being inherited from.
Child/Derived Class: The class that inherits from another class.
A child class gets all the attributes and methods of its parent.
A child class can override parent methods to provide its own specific implementation.
A child class can extend parent functionality using super().

# Code In Action:
```

# This is the PARENT class. It contains common attributes and methods.
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_logged_in = False

    def login(self):
        self.is_logged_in = True
        print(f"{self.username} has logged in.")

    def logout(self):
        self.is_logged_in = False
        print(f"{self.username} has logged out.")

# These are CHILD classes. They inherit from User.
class Admin(User): # The syntax for inheritance is ClassName(ParentClass)
    def __init__(self, username, email, permission_level):
        # 'super()' calls the __init__ of the parent (User) class
        super().__init__(username, email)
        self.permission_level = permission_level

    # This is a method only available to Admins
    def delete_user(self, other_user):
        print(f"Admin {self.username} is deleting user {other_user.username}.")

class Member(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.posts = []

    # This method is specific to Members
    def submit_post(self, content):
        self.posts.append(content)
        print(f"Post by {self.username} submitted.")

    # This method OVERRIDES the parent's method (though we're not doing it here)

# --- Creating objects ---
admin_user = Admin("s_admin", "admin@corp.com", 5)
member_user = Member("john_doe", "john@email.com")

admin_user.login() # This method is inherited from User
member_user.login()  # This method is also inherited

admin_user.delete_user(member_user) # This method only exists on the Admin class
member_user.submit_post("Hello world!") # This method only exists on the Member class

```

# Your Mission:

Create a base class Vehicle with an __init__ that takes make and model. It should also have a method get_info() that returns a string like "Make: Toyota, Model: Camry".
Create a Car class that inherits from Vehicle. Its __init__ should also take number_of_doors. It should override the get_info() method to add the number of doors to the output string. Use super().get_info() to avoid rewriting code.
Create a Motorcycle class that inherits from Vehicle. Its __init__ should also take type_of_bike (e.g., "Cruiser", "Sport"). It should also override get_info() to add the bike type.
Create one Car object and one Motorcycle object and print their info using the get_info() method to see the different outputs.