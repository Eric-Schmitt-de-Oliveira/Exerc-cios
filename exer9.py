p = input("Digite o valor da compra, se sua compra for maior que 100 terá desconto de 10%: ")
if float(p) > 100.00:
    print("O valor com desconto é:", float(p) * 0.9)
else:
    print("O valor com desconto é:", float(p) -float(p) * 0.1)