import os

# Define the start and end numbers for your file names.
start_number = 16
end_number = 25  # Change this value to create more or fewer files.

# Loop through the desired range and create an empty file for each number.
for i in range(start_number, end_number + 1):
    file_name = f"program{i}.py"
    # Check if file already exists to avoid overwriting
    if not os.path.exists(file_name):
        with open(file_name, 'w') as f:
            # Create an empty file; you could also write a comment or a placeholder.
            f.write("# This is " + file_name + "\n")
        print(f"Created {file_name}")
    else:
        print(f"{file_name} already exists")
