text_list = ['x', 'xxx', 'xxxxx', 'xxxxxxx', '']

f = lambda s: len(s)

print(list(map(f, text_list)))
print(list(map(lambda x: len(x), text_list)))
