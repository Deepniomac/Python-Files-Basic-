#Program to calculate the compound interest
principle = float(input("Enter the principle Value : "))
rate = float(input("Enter the rate : "))
compounded_value = float(input("Enter the compounded value per year : "))
time = float(input("Enter the time : "))

#compound interest formula 
amount =principle * pow ((1 + rate / compounded_value),time)
C = float(amount - principle)
print(f"Compound interest for {time:.2f} years is {C:.2f}")
