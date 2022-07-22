# if condition:
#     acao
#     acao

nota1= int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("Passou de ano") 
elif media < 6 and media >= 4:
    print("Você está de recuperação")   
else: 
    print("Reprovado")