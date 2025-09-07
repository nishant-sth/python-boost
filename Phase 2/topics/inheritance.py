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
