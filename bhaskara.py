import math

a = float(input("Digite o valor de a "))
b = float(input("Digite o valor de b "))
c = float(input("Digite o valor de c "))
delta = b**2 - 4*a*c
print("delta =", delta)
if delta < 0:     
    print("Não tem raiz!")
elif delta == 0:
    print("Uma raiz real!")
else:
    resp = input("Deseja calcula o valor da raízes? (s/n) ")
    while resp not in ["s", "n"]:
        resp = input("Opção inválida! Digite 's' ou 'n' ")
    if resp == "s":
        print("Você digitou", resp)
        x1 = (-b + math.sqrt(delta)) / (2*a)    
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(x1, x2)
    else: 
        print("Obrigado!")
    input("Pressione ENTER para sair...")