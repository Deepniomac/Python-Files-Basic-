#Program to calculate the simple interest
principle = int(input("Enter the principle Value : "))
time = int(input("Enter the time : "))
rate = int (input("Enter the rate : "))

#simple interest formula 
simple_interest = ( principle * time * rate )/ 100

print(f"Simple interest : {simple_interest}")
