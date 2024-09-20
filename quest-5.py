# Questão 5 
string = input("Digite uma palavra para inverter os caracteres: ")
string_invertida_for = " "

# Invertendo utilizando slicing 
string_invertida = string[::-1]

print(f'String invertida usando slicing: {string_invertida}')

for caractere in string:
    string_invertida_for = caractere + string_invertida_for

print(f'String invertida utilizando laços de repetição: {string_invertida_for}')