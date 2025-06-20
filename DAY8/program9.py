# This is program9.py


file1=open("Filesample.txt","w")

for i in range(3):
    name=input("Enter name: ")

    file1.write(name)
    file1.write("\n")


