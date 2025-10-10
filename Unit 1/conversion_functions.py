#program to implement type conversions

value = input("Enter a value : ")

#into string
str_val = str(value)
print("String :",str_val)

#into boolean
bool_val = bool(value)
print("Boolean :",bool_val)

#int and float
if value.isdigit() :
    int_val = int(value)
    print("Integer :",int_val)
    float_val = float(value)
    print("Float :",float_val)
else :
    print("Cannot be converted ! ")

#list to tuple
list1 = [7,8,9]
tuple1 = tuple(list1)
print(f"Tuple is : {tuple1}")

#string to tuple
str2 = str(tuple1)
print(f"String is : {str2}")


