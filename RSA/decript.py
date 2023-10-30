with open('Зашифрованный файл.txt',encoding='utf-8') as file:
    massage = file.read()

d, n = input('Введите закрытый ключ: ').split('|')
mass_massage = map(ord, massage)
secret_text = ''

for i in mass_massage:
    secret_text = secret_text + chr((int(i) ** int(d)) % int(n))

with open("Расшифрованный файл.txt", 'w', encoding='utf-8') as file:
    file.write(secret_text)