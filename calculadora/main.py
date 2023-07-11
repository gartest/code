from functions import add_numers, read_number

print("Ingrese número 1")
num1 = read_number()
print("Ingrese número 2")
num2 = read_number()
result = add_numers(num1, num2)

print(f"El resultado de {num1} + {num2} es: {result}")
