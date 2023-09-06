def get_password(password):
    pass_mass = list(map(ord, password))
    position = []
    for i in pass_mass:
        counter = 1
        for j in pass_mass:
            if j > i:
                counter += 1
        position.append(counter)

    for i in range(1, max(position)+1):
        if position.count(i) > 1:
            counter = 0
            for j in range(len(position)):
                if position[j] == i:
                    position[j] += counter
                    counter += 1

    return position

def encrypt_the_message(pas, massage):
    password = get_password(pas)
    massage = massage + ' ' * (len(password)-len(massage) % len(password))
    mass_massage = {}
    column_len = len(massage) // len(password)
    for i in range(0, len(massage), column_len):
        column = list(massage[i:i+column_len])
        mass_massage[password[i//column_len]] = column

    out_mass = []

    for i in range(1, len(mass_massage.keys())+1):
        out_mass.append(mass_massage[i])

    return out_mass
