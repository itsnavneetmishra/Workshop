# This is program8.py
file1=open("Filesample.txt","r")

print(file1.read())
print()

file1.seek(0)
print(file1.readline())
print()


print(file1.read(5))
print()

file1.seek(0)
print(file1.readlines())
print()