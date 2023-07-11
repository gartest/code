#user input
print("Ingrese números enteros separados por un espacio")
#leemos el input del usuario
user_input_str = input()
#convertimos el input del usuario a un arreglo
user_input_arr = user_input_str.split()
#imprimimos el arreglo
print(f"Los número ingresados son {user_input_arr}")
#Declaración de arreglos vacíos que usarémos durante la ejecución
even_numbers = []
positive_numers = []
odd_numbers = []
not_numbers = []

#Recorremos el arreglo de los datos ingresados por el usuario
for n in user_input_arr:
    try:
        #intentamos convertir el string a entero
        curr_num = int(n)
        #si es par lo agregamos al arreglo de números pares
        if(curr_num % 2 == 0):
            even_numbers.append(curr_num)
        #sino lo agregamos al arreglo de impares
        else:
            odd_numbers.append(curr_num)
        #si es mayor a cero lo agregamos al 
        if(curr_num > 0):
            positive_numers.append(curr_num)
    #si la conversión no funciona se lo indicamos al usuario y agregamos ese string a un array de "no números"
    except:
        print(f"{n} no es un número")
        not_numbers.append(n)

#Chequea el largo de los arrays para control de las salidas
even_numbers_len = len(even_numbers)
positive_numers_len = len(positive_numers)
odd_numbers_len = len(odd_numbers)
not_numbers_len = len(not_numbers)

#salida

print(f"haz ingresado {even_numbers_len} números pares")

if(positive_numers_len > 0):
    print(f"la suma de los números positivos es {sum(positive_numers)}") #sum es una función que suma los elementos de un array

if(odd_numbers_len > 0):
    #promedio
    avg = sum(odd_numbers) / len(odd_numbers)
    #modulo
    mod = sum(odd_numbers) % len(odd_numbers)
    print(f"El promedio de los número impares es {int(avg) if mod == 0 else avg}")

if(not_numbers_len > 0):
    print(f"haz ingresado {not_numbers_len} strings que no son números")
