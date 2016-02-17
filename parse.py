def only_numbers(text,floatingPoint=""):
    aux = ""
    for char in text:
        if (ord(char) > 47 and ord(char) < 58 or ord(char) == ord(floatingPoint)):
            aux = aux + char
    return aux

def only_letters(text):
    aux = ""
    for char in text:
        if not (ord(char) > 47 and ord(char) < 58):
            aux = aux + char
    return aux

def get_magnet_link(text):
    aux = ""
    cont = 0
    for char in text:
        if (char == '"'):
            cont = cont +1
        if (cont == 1):
            aux = aux + char
    return aux[1:]
