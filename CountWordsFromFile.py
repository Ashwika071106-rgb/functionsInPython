def countWordsFromFile() : 
    fileName = input("Enter the name of the file : ")
    file = open(fileName, 'r')
    numberOfWords = 0
    for line in file : 
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("Number of words = ")
    print(numberOfWords)


countWordsFromFile()