# Condicionales en Python
# Si el número ingresado esta dentro de un rango, y si esta en la primera o segunda mitad
# Primero declaramos una variable para guardar número, leemos lo que el usario ingresa después de pedirlo
numero = input(" == Ingresa un Número: ")
# Pasamos la variable a tipo int (entera)
numero = int(numero)
# Si el número es mayor o igual a 20 y menor o igual a 40
if numero >= 20 and numero <= 40 :
    # Imprimimos el siguiente mensaje
    print(" == El número esta dentro del rango! ==")
    # Creamos un if anidado
    # Si el número es mayor o igual a 20 y el número es menor o igual a 30
    if numero >= 20 and numero <= 30 :
        # imprimimos el siguiente mensaje
        print(" == El número pertenece a la primera mitad del rango de números")
    # Si por el contrario el número es mayor a 30 y menor o igual a 40
    elif numero > 30 and numero <= 30 :
        # Imprimimos el siguiente mensaje
        print(" == El número pertenece a la segunda mitad del rango de números")
# Si ninguna se las condiciones no se cumple
else :
    # Imprimimos qué el número no pertenece al rango
    print(" == El número no pertenece al rango (20 - 40) ==")