import time

start = time.process_time()
file = open("file.txt")
para = ""
wordCount = 0
k = -1
for x in file:
    para = para.strip() + " " + x
para = para.lower()
words = para.split()
for x in words:
    k = k + 1
    p = len(x) - 1
    if x[-1] == '.' or x[-1] == ',':
        words[k] = x[0:p]
for x in words:
    count = 0
    for y in words:
        if x == y:
            count = count + 1
    print("the frequency of ", x, "is ", count)
    wordCount = wordCount + 1
    words.remove(x)
print(time.process_time() - start)
print("number of unique words ", wordCount)
