text = 'hello'
print(list(zip(*[text[i:] for i in range(3)])))
