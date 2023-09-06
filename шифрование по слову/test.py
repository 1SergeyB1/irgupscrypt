from encryptor import *


password = 'Pa$$w0rd'
with open('text.txt', encoding='utf-8') as f:
    text = f.read()
secret_massage = encrypt_the_message(password, text)
text = ''
for i in range(len(secret_massage[0])):
    for j in range(len(secret_massage)):
        text = text + secret_massage[j][i]

with open('шифровка.txt','w',encoding='utf-8') as f:
    f.write(text)