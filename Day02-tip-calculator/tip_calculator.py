# Tip Calculator Project
# If the bill was $150.00, split between 5 people, with a 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# After formatting the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_bill = bill * (1 + tip / 100)
bill_per_person = total_bill / people
#final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${bill_per_person:.2f}")