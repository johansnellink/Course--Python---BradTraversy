# Python has functions for creating, reading, updating, and deleting files.


# Open/Create a file
myFile = open('myFile.txt', 'w')

# Get info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and Javascript')
myFile.close()

# Append to file
myFile = open('myFile.txt', 'a')
myFile.write(' I also like React :P')
myFile.close()

# Read from file
myFile = open('myFile.txt', 'r+')
text = myFile.read(10)
print(text)