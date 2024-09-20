# Questão 2
def fibonacci(n):
    a,b = 0,1
    while a <= n: 
        if a == n: 
            return True 
        a, b = b, a + b
    return False 

def input_inteiro():
    while True:
        try: 
            return int(input("Informe um número inteiro: "))
        except ValueError: 
            print("Entrada inválida! Por favor, digite um número inteiro.")

numero = input_inteiro()

if fibonacci(numero):
    print(f"O número {numero} pertence a sequência de fibonacci.")
else:
    print(f"O número {numero} não pertence a sequencia de fibonacci")