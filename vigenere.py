import string
string.printable = string.printable.replace("\r", "à")

def cesar_ciffer(message, key):
    if type(key) != int:
        print("la clef doit être un entier")
        return None

    message = str(message)
    list_of_crypted_caracs = []

    for carac in message:
        crypted_index = (string.printable.index(carac) + key) % len(string.printable)
        crypted_carac = string.printable[crypted_index]
        list_of_crypted_caracs.append(crypted_carac)

    crypted_message = "".join(list_of_crypted_caracs)
    return crypted_message

def cesar_decrypt(crypted_message, key):
    return cesar_ciffer(crypted_message, -key)

def vigenere(message, password, ciffer):
    if ciffer:
        list_of_keys = [string.printable.index(password_carac) for password_carac in password]
    else:
        list_of_keys = [- string.printable.index(password_carac) for password_carac in password]

    list_of_crypted_caracs = []

    for index_carac, carac in enumerate(message):
        current_key = list_of_keys[index_carac % len(list_of_keys)]
        list_of_crypted_caracs.append(cesar_ciffer(carac, current_key))

    crypted_message = "".join(list_of_crypted_caracs)
    return crypted_message