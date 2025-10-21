#python program to add content to an existing file
with open("sample.txt", "a") as file :
    file.write("hi python programming\n")
print("Content added to the file successfully.")