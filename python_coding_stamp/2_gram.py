text = 'hello'

for i in range(len(text)-1):
    print(text[i], text[i+1], sep = '')

two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep = '')

text = 'this is python script'
words = text.split()

for i in range(len(words)-1):
    print(words[i], words[i+1])

print(list(zip(words, words[1:])))
