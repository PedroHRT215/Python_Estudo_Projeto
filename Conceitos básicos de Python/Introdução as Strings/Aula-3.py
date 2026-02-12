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
print(my_str_1[1:4]) #ell
#O índice stop é não inclusivo, nesse caso o [1:4] extraiu apenas os 
#caracteres do índice de 1, sem incluir o 4, o caracter de índice 4. 

#Também pode omitir os índices start e stop, o Python utiliza 0 por padrão ou
#o final da string, respectivamente.
#Isso ocorre quando omitir o índice start:
print(my_str_1[:7]) #Hello W

#Isso ocorre quando omitir o índice stop:
print(my_str_1[8:]) #rld

#Caso omitir ambos:
print(my_str_1[:]) #Hello World

#Além de start e stop, temos o índice step, usado para especificar o incremento
#entre cada índice no slice. 
    #string[start:stop:step]

print(my_str_1[0:11:2]) #Hlowrd
    #No exemplo acima, o fatiamento começa no índice 0, para antes de 11 e 
    #extrai a cada 2 caractere

#Um truque útil para fazer com o parâmetro step é inverter uma string
#definindo o step como -1 e omitindo o start e stop
print(my_str_1[::-1]) # dlrow olleH
