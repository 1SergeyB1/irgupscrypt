password = '1+4+3+0+2+2+4+0+1+3'
password = password.split('+')
pass_len = len(password) // 2

column = password[:pass_len]
lines = password[pass_len:]

with open('зашифрованный текст.txt', encoding='utf-8') as file:
    massage = file.read()

mass_massage = []
for i in range(pass_len):
    line = []
    for j in range(pass_len):
        line.append(massage[i * pass_len + j])
    mass_massage.append(line)


new_mass = [[] for i in range(pass_len)]

for i in range(pass_len):
    new_mass[i] = mass_massage[int(lines[i])]
mass_massage = new_mass

for i in range(pass_len):
    r = []
    for j in column:
        r.append(mass_massage[i][int(j)])
    mass_massage[i] = r

text = ''

for l in mass_massage:
    text = text + ''.join(l)

with open('Расшифрованный текст.txt','w',encoding='utf-8') as file:
    file.write(text)