def password():
    import string
    from random import choice, randint
    char_number = 13
    chars = string.ascii_letters + string.digits
    password = "".join(choice(chars) for x in range(randint(char_number, char_number)))
    return password