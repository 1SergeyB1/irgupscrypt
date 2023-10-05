with open('Шифр.txt', encoding='utf-8') as file:
    text = file.read()
with open('Гамма.txt', encoding='utf-8') as file:
    gamma = int(file.readline().removesuffix('\n'))
    max_len = int(file.readline().removesuffix('\n'))

encript_bit_text = ''
line = ''

for letter in  text:
    bin_letter = "{0:b}".format(ord(letter))
    bin_letter = '0'*(max_len-len(bin_letter)) + bin_letter
    line = line + bin_letter
    if len(line) > 64:
        encript_bit = "{0:b}".format(int(line[:64], 2) ^ gamma)
        encript_bit = '0' * (64 - len(encript_bit)) + encript_bit
        encript_bit_text = encript_bit_text + encript_bit
        line = ''

encript_text = ''

for i in range(0, len(encript_bit_text) - max_len, max_len):
    encript_text = encript_text + chr(int(encript_bit_text[i:i+max_len], 2))

with open('расшифрованный_текст.txt','w',encoding='utf-8') as file:
    file.write(encript_text)
