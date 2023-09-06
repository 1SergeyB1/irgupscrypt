from encryptor import get_password
with open('шифровка.txt', encoding='utf-8') as f:
    text = f.read()
password = 'Pa$$w0rd'
text_mass = [[] for j in range(len(password))]

for i in range(len(text)):
    text_mass[i % len(password)].append(text[i])

encrypt_password = get_password(password)


text = ''
for i in encrypt_password:
    text = text + ''.join(text_mass[i-1])
print(text)