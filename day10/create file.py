import os

start_number = 1
end_number = 10

for i in range(start_number, end_number + 1):
    file_name = f"program{i}.py"
    if not os.path.exists(file_name):
       
        print(f"Created {file_name}")
    else:
        print(f"{file_name} already exists")
