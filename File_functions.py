#open function to open the file "test.txt"
f = open("test.txt")

#reading the file
f1 = f.read()
print(f1)

#reading the file line by line
f2 = f.readlines()
for line in f2 : 
    print(line)