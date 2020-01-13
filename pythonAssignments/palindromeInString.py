str = input("Enter a string:")
wordsList = str.split()
length = 0
for word in wordsList:
    word1 = word[::-1]
    if word1 == word:
        len1 = len(word)
        if len1 > length:
            length = len1
            palinLarge = word
if length == 0:
    print("No palindrome in the given string")
    print(wordsList)
else:
    txt = "The longest palindrome in the given string is {} and has a length of {}"
    print(txt.format(palinLarge,length))
