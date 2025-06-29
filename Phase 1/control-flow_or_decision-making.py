# if/elif/else: Check a user's permission level
user_role = "admin"

if user_role == "admin":
    print("Full access granted.")
elif user_role == "editor":
    print("Can write and edit posts.")
else:
    print("Read-only access.")

# for loop: Print all items in a shopping cart
cart_items = ["Milk", "Bread", "Eggs"]
print("\nItems in your cart:")
for item in cart_items:
    print(f"- {item}")

# while loop: A simple countdown
count = 3
while count > 0:
    print(f"{count}...")
    count -= 1 # Crucial: Don't forget to change the condition variable!
print("Go!")