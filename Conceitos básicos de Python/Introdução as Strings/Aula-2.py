#O que são concatenação de strings e interpolação de strings?
#Em Python é possível combinar várias strings usando o operador de adição (+). 

my_str_1 = 'Hello'
my_str_2 = 'World'

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) #Hello World

#Porém só funciona com strings, caso tentar concatenar uma string com um número, ocorrerá um "TypeError"
nome = 'Pedro'
idade = 20

'''name_and_age = nome + '' + idade
#print(name_and_age) # TypeError: can only concatenate str (not "int") to str

#Esse erro ocorre devido ao Python não converter automaticamente outros tipos de dados,
#exigindo que os dados sejam convertidos em strings antes de concatená-los. '''

#Porém, é possível realizar a conversão das seguintes maneiras:

#str(): função integrada 'concat', que retorna em string do objeto fornecido sem modificar o original:
name_and_age = nome + ' ' + str(idade)
print(name_and_age) #Pedro 20

#Ou podemos utilizar o operador de atribuição aumentada para a concatenação. Sendo esse representado
#por um sinal +=, onde realiza a concatenação e atribuição em uma única etapa. 

nome2 = 'Pedro '
idade2 = 20

name_and_age2 = nome2 #Começa com o nome
name_and_age2 += str(idade2)

print(name_and_age2) 

#Agora existe o processo de inserir váriaveis e expressões em uma string, sendo chamado de interpolação de strings.
#Python possui uma categoria de strings chamad f-strings (abreviação de literais de strings formatados), que permite lidar 
#com a interpolação usando uma sintaxe compacta e legível.

#As f-strings começam com f(em minúsculas ou maísuculas) antes das aspas e permitem inserir variáveis ou expressões dentro
#de campos de substituição indicados por chaves {}. 

nome3 = 'Pedro'
idade3 = 20

name_and_age3 = f'My name is {nome3} and I am {idade3} years old'
print(name_and_age3)

num1= 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}')#A soma de num1 + num2 é 15

#Percebe que não é necessário converter as não strings com str(), pois as variáveis não strings são convertidos internamente em string 
#durante o processo de interpolação. 
