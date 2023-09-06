from math import sqrt, ceil
from random import shuffle

with open('не шифрованный текст.txt', encoding='utf-8') as file:
    massage = file.read()

mass_size = ceil(sqrt(len(massage)))
mass_massage = []

massage = massage + ' ' * (mass_size ** 2 - len(massage))

for i in range(mass_size):
    line = []
    for j in range(mass_size):
        line.append(massage[i*mass_size+j])
    mass_massage.append(line)

column = [i for i in range(mass_size)]
shuffle(column)
line = [i for i in range(mass_size)]
shuffle(line)

for l in range(mass_size):
    r = []
    for i in range(mass_size):
        r.append(mass_massage[l][column.index(i)])
    mass_massage[l] = r

new_mass = []
for i in range(mass_size):
    new_mass.append(mass_massage[line.index(i)])
mass_massage = new_mass
text = ''

for l in mass_massage:
    text = text + ''.join(l)

with open('зашифрованный текст.txt','w',encoding='utf-8') as file:
    file.write(text)

print('+'.join(list(map(str, column))) + '+' + '+'.join(list(map(str, line))))