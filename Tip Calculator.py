print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
total_bill = bill * (1 + tip / 100)

# Calculate the amount per person
amount_per_person = total_bill / people

# Format the result to 2 decimal places
formatted_amount = "{:.2f}".format(amount_per_person)

# Print the final amount each person should pay
print(f"Each person should pay: ${formatted_amount}")
