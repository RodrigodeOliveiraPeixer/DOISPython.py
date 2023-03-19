#2 -  Solicitar 5 números, ao fim, imprimir o número maior e o número menor.

lista = []

for i in range(5):
    numero= float(input("Digite o número : "))
    lista.append(numero)
    

print('O maior numero digitado foi: {:.1f} '.format(max(lista)))
print('O menor numero digitado foi: {:.1f} '.format(min(lista)))
