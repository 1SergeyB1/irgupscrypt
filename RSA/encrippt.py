with open('text.txt',encoding='utf-8') as file:
    massage = file.read()

e, n = input('Введите открытый ключ: ').split('|')
mass_massage = map(ord, massage)
secret_text = ''

for i in mass_massage:
    secret_text = secret_text + chr((int(i) ** int(e)) % int(n))

with open("Зашифрованный файл.txt", 'w', encoding='utf-8') as file:
    file.write(secret_text)
