# FILE ANALYZER WITH FREQUENCY COUNTING
f = open('myfile.txt', 'r')
text = f.read()
lines = text.split('\n')
words = text.split()
print(f"words: {len(words)}")
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

# print(f"text: {len(words)} ")
print(f"lines: {len(lines)}")
print(text)
most_common = max(word_count, key = word_count.get)
print(f"most common : {most_common}")
print(f"word count : {word_count[most_common]}")
    