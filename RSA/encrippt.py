

def enript_massage(e ,n , way_to_file):
    with open(way_to_file, encoding='utf-8') as file:
        massage = file.read()
    mass_massage = map(ord, massage)
    secret_text = ''

    for i in mass_massage:
        secret_text = secret_text + chr((int(i) ** int(e)) % int(n))

    return secret_text
