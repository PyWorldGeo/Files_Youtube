# File Creation
try:
    file = open("new.txt", "x")
    file.close()
except:
    print("File already exists!")

# File Reading
file = open("new.txt", "r")
data = file.read()
print(data)
file.close()

# File writing
file = open("new.txt", "w")
file.write("I am Groot!")
file.close()

# File Append
file = open("new.txt", "a")
file.write("\nI am Groot!")
file.close()

#Closing file automatically
with open("new.txt", "r") as file:
    data = file.read()

print(data)

#Write and read same time
with open("new.txt", "r+") as file:
    file.write("Hi")
    data = file.read()

print(data)

#Read separate lines
with open("new.txt", "r") as file:
    print(file.readline(3))
    print(file.readline(5))
    print(file.readline(2))
    print(file.readline())
    print(file.readline())

#Loop throught lines
with open("new.txt", "r") as file:
    for line in file.readlines():
        print(line)
#Creating file with write method
with open("new.txt", "w") as file:
    file.write("Exists")