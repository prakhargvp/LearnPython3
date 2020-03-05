from sys import argv

script_name, filename = argv

# Some of the operation we can perform on file
# read, readLine, truncate, write, seek

# Print the filename
# To use f literal python version should be 3.6 or higher
print(f"File : {filename}")

# Open & Read the file
file = open(filename)

print(file.read())

# Close the file
file.close()