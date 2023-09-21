from random import randint

gamma = randint(9223372036854775808, 18446744073709551615)

with open('текст.txt', encoding='utf-8') as file:
    text = file.read()

bit_mass = []
max_len = 0
bit_text = ''

for letter in text:
    letter_bit = "{0:b}".format(ord(letter))
    bit_mass.append(letter_bit)
    if len(letter_bit) > max_len:
        max_len = len(letter_bit)

for i in range(len(bit_mass)):
    if len(bit_mass[i]) < max_len:
        bit_text = bit_text + '0' * (max_len-len(bit_mass[i])) + bit_mass[i]
    else:
        bit_text = bit_text + bit_mass[i]

encript_text = ''
for i in range(0, len(bit_text)-64, 64):
    text = "{0:b}".format(int(bit_text[i:i+64], 2) ^ gamma)
    text = '1' + '0' * (64 - len(text)) + text
    for j in range(0, len(text), 5):
        encript_text = encript_text + chr(int(text[j:j + 5], 2))

with open('Гамма.txt', 'w') as file:
    file.write(str(gamma))

with open('Шифр.txt', 'w') as file:
    file.write(encript_text)

print(max_len)