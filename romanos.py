def convertir_en_romano(numero):
    """
    Restricciones:
        - Es un numero natural
        - El numero este entre 0 y 3999
            - no es negativo
            no es mayor de 3999
    Resulatdo de una cadena que contiene (I, V, X, L, C, D, M)
    
    Ideas para comprobar un entero:
        - (X) isdigit(): porque no aplica a cualquier cosa que no sea cadena
        - (V) coventir a int y si no se puede error
        - (V) isinstance()
        - (V) type()
        - (X) isnumeric()

    PASOS:
        1. Validando la entrada
        2a. Si es válido: lo convierto
        2b. Si no es válido: muestro un error
    """

    #try:
        #numero_validado = int(numero)
    #except ValueError:
        #raise  ValueError (f"{numero} no es número válido")

    if not isinstance(numero, int) or numero < 0 or numero > 3999:
        return "El número introducido no es válido (debe ser positivo y menor de 4000)"

print(convertir_en_romano("3a3"))
print(convertir_en_romano(-3))
print(convertir_en_romano(3333))
# convertir_en_romano(-3)
# convertir_en_romano("a")