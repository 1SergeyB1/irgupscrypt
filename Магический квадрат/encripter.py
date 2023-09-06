magic_squarer = [16, 3, 2, 13,
                 5, 10, 11, 8,
                 9, 6, 7, 12,
                 4, 15, 14, 1]
with open('текст.txt',encoding='utf-8') as file:
    massage = file.read()

if len(massage) > 16:
    massage = massage + ' ' * ((len(magic_squarer) - len(massage) % len(magic_squarer)))
else:
    massage = massage + ' ' * (len(massage) % len(magic_squarer))

text = ''
for i in range(len(massage)//len(magic_squarer)):
    table = [t for t in range(len(magic_squarer))]
    for j in range(len(magic_squarer)):
        table[magic_squarer.index(j + 1)] = massage[i*len(magic_squarer) + j]
    text = text + ''.join(table)

with open('зашифрованный файл.txt','w',encoding='utf-8') as file:
    file.write(text)