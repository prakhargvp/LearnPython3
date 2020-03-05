from sys import argv
from os.path import exists

script_name, from_file, to_file = argv


# Open the input file and read the file
fromFile = open(from_file)
fromFileData = fromFile.read()
print(f"The input file {from_file} is {len(fromFileData)} bytes long")
print(f"Does the output file exists ? {exists()}")
print("Hit Enter to Copy Data from {from_file} to {to_file} Else CTRL-C to abort")

# Open to file in write (w) mode
toFile = open(to_file, "w")
toFile.write(fromFileData)

print("Succesfully copied data from one file to other")
toFile.close()
fromFile.close()
