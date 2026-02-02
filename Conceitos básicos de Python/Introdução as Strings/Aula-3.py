#O que é o fatimaneto de strings e como funciona?

#Em aulas anteriores aprendemos que cada caractere em uma string pode ser
#identificado por seu ínidice(começando do zero) e acessando usando a notação dos colchetes.

my_str = "Hello World"

print(my_str[0]) #H
print(my_str[6]) #W
print(my_str[-1]) #d

#O fatiamento de strings permite extrair uma orção de uma string ou trabalhar apenas
#com uma parte específica dela.
#string[start:stop]

#Se quiser extrair caracteres de um determinado índice para outro,
#basta separar os start e stop com dois pontos
my_str_1 = "Hello World"
print(my_str_1)