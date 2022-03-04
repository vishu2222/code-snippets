# read a file
f = open("new.txt", "r")
line1 = f.readline()


# Read line by line
f = open("new.txt", "r")
for i in f:
  print(i)
