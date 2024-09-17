from itertools import count

word="PROGRAMMING"
used_chars = {'a','e','i','o''u'}
for i in range(count(word)):
    if word[i] in used_chars:
        used_chars[word[i]] = i
    print(i)
