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
top_n = int(input("how many top words do you want to see "))
sorted_words = sorted(word_count, key = word_count.get, reverse = True)
print(f"top {top_n} words:")
for word in sorted_words[:top_n]:
    print(f"{word} : {word_count[word]}")