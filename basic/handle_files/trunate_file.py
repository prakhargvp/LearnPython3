from sys import argv

script_name, filename = argv

print(f"Are You Sure you want to erase the file : {filename} ")
print("If not press CTRL-C (^c)")
print("If you do want, hit Enter")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file...")
target.truncate()

# If you want to write the file

print("Add Content in the file : ")
data = input()

target.write(data)
target.write("\n")

print("Finally, close the file")
target.close()
