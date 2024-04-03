import os

fileName = input("enter file name")
content = input("provide content")

isExist = os.path.exists(fileName)

if isExist:
    with open(fileName,'a') as file:
        file.write(f"\n{content}")
else:
    with open(fileName,'w') as file:
        file.write(content)

isRead = input("do you wanna read? enter y or n")

if isRead == "y":
    with open(fileName, 'r') as file:
        print(file.read())