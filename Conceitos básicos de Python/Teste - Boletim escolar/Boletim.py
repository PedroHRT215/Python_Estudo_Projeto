#Passo 1:
#Criar uma variável chamada name e atribuir a ela a string Alice
name = "Alice"

#Passo 2:
#Usar a função print() para exibir a variável acima
#print(name)

#Passo 3:
#Usar a função type() para validar o tipo da variável name
#print(type(name))

#Passo 4:
#O boletim deve indicar se o aluno está matriculado. 
#No caso vai ser utilizado o valor booleano para determinar o fato.
#Criar uma variável e atribuir o valor true
is_student = True

#Passo 5: 
#Printar o valor e o tipo da variável is_student, separando com ,.
print(is_student, type(is_student))

#Passo 6:
#Remover as saídas da variável name e subsituir igual ao passo 5.
print(name, type(name))

#Passo 7:
#Adicionar uma idade ao aluno utilizando um int e variável int, 
#atribuir o valor 20. 
age = 20
print(age, type(age))

#Passo 8:
#Adicionar a variável score e atribuir o valor 80.5
#e utilizar a função isistance() para verificar se score 
#é int, pois, age e score não podem ser do mesmo tipo.
score = 80.5
#print(isinstance(score, int))

#Passo 9:
#Subnstituir int por float no print acima e 
#indicar o tipo da variável score
print(isinstance(score, float))
print(score, type(score))


#Saída:
'''

True <class 'bool'>
Alice <class 'str'>
20 <class 'int'>
True
80.5 <class 'float'>

'''

