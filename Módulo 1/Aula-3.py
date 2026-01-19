#Quais são os tipos de dados comuns em Py e como obter o tipo de uma variável?

"""
Em Py não precisa declarar o tipo da variável, pois é uma linguagem de tipagem dinâmica,
ou seja, a linguagem sabe o tipo de dado de uma variável com base no valor atribuido
"""

nome = 'Pedro' #Python sabe que se trata de uma string
idade = 20 #Python sabe que se trata de uma int

#Essa tipagem torna a programação mais rápida e flexível, porém pode levar a erros inesperados.
"""
Como o Py determina os tipos de dados durante a execução do programa, erros relacionados
a tipos só são detectados nesse momento. Quando um programa é executado, o Python processa
o código linha por linha, se ele chegar em uma linha que determinado objeto deveria se comportar 
de uma maneira que não consegue, o Python irá parar e exibir um erro.  


A ideia importante é:
-Em Python, erros de digitação podem se manifestar durante a execução, 
quando o programa está efetivamente rodando e utilizando o seu código.

-Linguagens compiladas detectam erros de tipo durante a etapa de compilação, 
antes que o programa possa ser executado.
"""

#Aqui estão os tipos de dados mais comuns em Python:

#Número inteiro: um número sem decimais, ex: 10 ou -5
my_int_var = 10
print('Int:', my_int_var) #Int:10

#Número de ponto flutuante: um número com um ponto decimal, ex: 4.42 ou -0.4
my_float_var = 4.50
print('Float:', my_float_var) 

#String: sequência de caracteres delimitada por '' ou "", ex:'Hello Word!'
my_string_var = 'Hello Word!'
print('String:', my_string_var)

#Booleano: Um tipo verdadeiro ou falso, escrito como True ou False
my_boolean_var = True
print('Boolean:', my_boolean_var)

#Contjunto: Uma coleção não ordenada de elementos únicos, como {4,2,0}
my_set_var = {7,5,8}
print('Set:', my_set_var)

#Dicionário: Uma coleção de pares chave-valor delimitados por chaves, como
#{'name': 'Pedro Henrique', 'age': 28}
my_dictionary_var = {'nome': 'Pedro Henrique', 'age': 20}
print('Dictionary:', my_dictionary_var)

#
