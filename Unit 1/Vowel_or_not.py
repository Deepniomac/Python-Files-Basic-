#python program to check whether the given letter is vowel or not
ch = input("Enter a letter: ")
if ch in "aeiouAEIOU":
    print(f"The letter '{ch}' is a vowel")
else :
    print(f"The letter '{ch}' is not a vowel")