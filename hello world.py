def read_number():
    user_input = input()
    while(not user_input.isnumeric()):
        print("Por favor ingresa un número")
        user_input = input()
    return int(user_input)

def add_numers(a,b):
    return a + b

print("Ingrese número 1")
num1 = read_number()
print("Ingrese número 2")
num2 = read_number()
result = add_numers(num1, num2)

# print("El resultado de %d + %d es: %d" % (num1, num2, result))
print(f"El resultado de {num1} + {num2} es: {result}")
