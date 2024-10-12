print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100
total_bill_with_tip = (total_bill * tip_percentage) + total_bill
divided_bill = total_bill_with_tip / total_people
print(f"Each person should pay: ${round(divided_bill, 2)}")