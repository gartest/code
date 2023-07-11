def read_number():
    user_input = None
    number = None
    while(True):
        try:
            user_input = input()
            number = int(user_input)
            break
        except:
            print("Por favor ingresa un número")
    return number


def add_numers(a,b):
    return a + b
