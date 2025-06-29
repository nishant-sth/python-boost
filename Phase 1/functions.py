def calculate_total_price(price: float, tax_rate: float, discount: float = 0) -> float:
    """
    Calculates the final price of an item including tax and applying a discount.
    This is a docstring - a good practice for explaining what a function does.
    """
    if not (0 <= tax_rate <= 1):
        raise ValueError("Tax rate must be between 0 and 1.")

    price_with_tax = price * (1 + tax_rate)
    final_price = price_with_tax * (1 - discount)
    return final_price

# Using the function
book_price = calculate_total_price(price=20.00, tax_rate=0.05)
print(f"The book costs: ${book_price:.2f}")

tv_price = calculate_total_price(price=500.00, tax_rate=0.08, discount=0.10)
print(f"The discounted TV costs: ${tv_price:.2f}")

# Example with *args and **kwargs
def create_user_profile(username, email, *extra_info, **profile_details):
    print(f"Creating user: {username} ({email})")
    print("Extra info provided:", extra_info)
    print("Profile details:", profile_details)

create_user_profile(
    "jdoe",
    "jdoe@email.com",
    "Loves Python",     # This goes into *args
    "Is a developer",   # This also goes into *args
    location="USA",     # This goes into **kwargs
    member_since=2024   # This also goes into **kwargs
)