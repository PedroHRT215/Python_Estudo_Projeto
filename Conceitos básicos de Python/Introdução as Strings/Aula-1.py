#O que são Strings e o que é Imutabilidade de String

""" 
    String: sequência de caracteres cercada por '' ou "". Diferente de outras linguagens,
    em Python ambas as aspas são tratadas de forma igual. Ou seja, pode usar ambas ao trabalhar 
    com strings
"""

#Segue alguns exemplos:
my_str_1 = 'Hello'
my_str_2 = "World"

#Se precisar de strings de múltiplas linhas utilize:
my_str_3 = """Multilinha
string"""
    #Multilinha
    #string

my_str_4 = '''Outra
string
multilinha'''
    #Outra
    #string
    #multilinha

#Se a string possui aspas simples ou duplas, temos 2 cenários:
    #Use o tipo oposto. Ou seja, se a string possui '', utlize "" 
    #para envolver a string e vice-versa:
msg = "It's a sunny day"
quote = 'Ele disse, "Olá Mundo"'
    #Também possui o método da \, com esse método pode
    #usar '' ou "" para envolver a própria corda
msg = 'It\'s a sunny day'
quote = "Ele disse, \"Olá Mundo\""


'''
Às vezes, pode ser necessário validar se uma string contém um ou mais caracteres.
Para isso, utiliza-se o operador in, que retorna um booleano para validar
se o/os caractere(s) existem ou não na string
'''
my_str_5 = 'Hello World'
print('Hello' in my_str_5) #True
print('hey' in my_str_5) #False
print('e' in my_str_5) #True
print('f' in my_str_5)#False


'''
Agora, vejamos como pode obter o comprimento de uma string e trabalhar
com os caracteres individuais de uma string, um processo chamado indexação.
Para obter o comprimento, basta usar a função embutida len().
'''
my_str_6 = 'Hello World'
print(len(my_str_6)) #11
#Considera espaço em branco como caractere

'''
Cada caractere de uma string possui uma posição denomida índice. 
índice: é baseado em 0, ou seja, o primeiro caractere de uma string será 0,
o segundo será 1 e assim por diante
'''
#Para acessar um caractere pelo seu índice, usa-se [].
my_str_7 = "Hello World"
print(my_str_7[0]) #H
print(my_str_7 [6]) #W

#Também pode haver a indexação negativa:
print(my_str_7 [-1])#d
print(my_str_7 [-2])#l

'''
Algumas linguagens agrupam os tipos de dados como primitivos ou de referência.
-Primitivo: simples e imutáveis, ou seja, não podem ser alterados depois de serem
-declarados.
-Referência: podem conter múltiplos valores e são mutáveis ou imutáveis.
Em python, todos os dados são tratados como objetos, sendo alguns mutáveis e outros
imutáveis. 

Como já dito, dados imutáveis não podem ser alterados após declarados. 
Mas pode apontar as variáveis desses objetos para algo novo, sendo chamado
esse processo de reassignment, mas não pode alterar o objeto original adicionado,
removendo ou substituindo qualquer um de seus elementos.

No caso, strings são do tipo imutáveis em Python. Significa que pode reatribuir uma
string diferente a uma variável:
'''
#Exemplo:
greeting = 'hi'
greeting = 'hello'
print(greeting) #hello

#Mas a modificação direta de uma string não é permitida:
greeting = 'hi'
greeting [0] = 'H'
#TypeError: 'str' object does not support item assignment