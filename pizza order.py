print("Welcome to Python Pizza Deliveries!")

# Get user choices
size = input("What size pizza do you want? (S, M, or L): ").upper()
add_pepperoni = input("Do you want to add pepperoni? (Y or N): ").upper()
extra_cheese = input("Do you want extra cheese? (Y or N): ").upper()

# Set base prices
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2  # Small pepperoni price
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3  # Medium/Large pepperoni price
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3  # Medium/Large pepperoni price
else:
    print("Invalid pizza size! Please enter S, M, or L.")
    exit()

# Add extra cheese
if extra_cheese == "Y":
    bill += 1

# Print the final bill
print(f"Your final bill is: ${bill}")


