with open('Шифр.txt',encoding='utf-8') as file:
    text = file.read()
with open('Гамма.txt',encoding='utf-8') as file:
    gamma = int(file.read())
max_len = 14

encript_bit_text = ''
encript_mass = []
for i in range(0, len(text) - 13, 13):
    block = text[i:i+13]
    line = ''
    for j in block:
        bin_form = '{0:b}'.format(ord(j))
        if len(bin_form) < 5:
            bin_form = '0' * (5 - len(bin_form)) + bin_form
        line = line + bin_form

    text_line = "{0:b}".format(int(line[1:], 2) ^ gamma)
    encript_bit_text = encript_bit_text + '0' * (64 - len(text_line)) + text_line

encript_text = ''
for i in range(0, len(encript_bit_text) - max_len, max_len):
    encript_text = encript_text + chr(int(encript_bit_text[i:i+max_len], 2))

print(encript_text)
