# Montando Triangulos

print("-" * 30)

lado1 = int(input("Diga o primeiro lado do triângulo: "))
lado2 = int(input("Diga o segundo lado do triângulo: "))
lado3 = int(input("Diga o terceiro lado do triângulo: ")) 
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2: 
    print("Forma um triangulo!")
    if lado1 == lado2 == lado3:
        print("O triangulo é equilátero!")
    elif lado1 != lado2 != lado3: 
        print("O triânngulo é escaleno")
    else: 
        print("O triângulo é isósceles")
else: 
    print("Não forma um triângulo!")

print("-" * 30)