introString = input("Enter about yourself: ")
interoString = int(input("Enter your Age: "))

characterCount = 0

wordCount = 1

for i in introString: 
    characterCount = characterCount + 1

    if(i==' '):
        wordCount = wordCount + 1
        

print("Number Of Words In String: ")
print(wordCount)
print("Number of Character In The String: ")
print(characterCount)
print(interoString)