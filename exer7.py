numb1 = input("Insira o primeiro número: ")
numb2 = input("Insira o segundo número: ")
numb3 = input("Insira o terceiro número: ")

if numb1 > numb2 and numb1 > numb3:
    print("O maior número é:", numb1)
    if numb2 > numb3 and numb2 > numb1:
        print("O maior número é:", numb2)
else:
    if numb2 > numb3:
        print("O maior número é:", numb2)
    else:
        print("O maior número é:", numb3)