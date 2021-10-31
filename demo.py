def countWordsFromFile():
    fileName=input('enter file name: ')
    numberOfWords=0
    file=open(fileName,'r')
    for line in file:
        word=line.split()
        numberOfWords=numberOfWords+len(word)
    print(numberOfWords)
countWordsFromFile()