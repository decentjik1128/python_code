word = input('단어를 입력하세요: ')

is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[-1-i]:
        is_palindrome = False
        break
print(is_palindrome)

word = input('단어를 입력하세요: ')
print(word == word[::-1])

word = input('단어를 입력하세요: ')
print(list(word) == list(reversed(word)))

word = input('단어를 입력하세요: ')
print(word == ''.join(reversed(word)))
