magic_squarer = [16, 3, 2, 13,
                 5, 10, 11, 8,
                 9, 6, 7, 12,
                 4, 15, 14, 1]

with open('зашифрованный файл.txt',encoding='utf-8') as file:
    text = file.read()

out = ''
for i in range(0,len(text),len(magic_squarer)):
    dicript_mass = [i for i in range(len(magic_squarer))]
    for j in range(i, i+len(magic_squarer)):
        dicript_mass[magic_squarer.index(j % len(magic_squarer) + 1)] = text[j]
    out = out + ''.join(dicript_mass)

print(out)