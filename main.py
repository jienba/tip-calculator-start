print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $ "))

percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100

numberOfPeople = int(input("How many people to split the bill? "))

totalBill = bill (1 + percentage) 

print(f"Each person  should pay : ${round(totalBill / numberOfPeople, 2)}")
