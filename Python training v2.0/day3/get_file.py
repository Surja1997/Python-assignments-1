from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as data:
    all_words=[]
    lines=[]
    for line in data:
        lines.append(line)
        for words in line.decode():
            all_words.append(words)
    print(lines)
    print(all_words)