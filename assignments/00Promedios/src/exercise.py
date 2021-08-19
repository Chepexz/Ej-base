import os
def main():
    os.system("clear")
    #escribe tu código abajo de esta línea
    print("Promedio de 10 números")
    suma=0
    total_pares=0
    total_impares=0
    for i in range(10):
        numero=int(input("Dame un número: "))
        if numero % 2 == 0:
            total_pares = total_pares + i
        else:
            total_impares = total_impares + i

        suma += numero

    promedio = suma/10
    print(f"El promedio de los valores capturados es {promedio}")        
    print(f"El total de valores pares fue: {total_pares}")        
    print(f"El total de valores impares fue: {total_impares}")        


if __name__=='__main__':
    main()
