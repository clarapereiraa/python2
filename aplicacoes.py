import time

#Encontrar maior valor na lsita - Exemplo 1
lista = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior_numero = list[0] #recebeu o numero 17 

for i in range(1, len(lista)):
    if lista[i] > maior_numero:
      maior_numero = lista[i]
print("o maior numero da lista é:", maior_numero)

#Exemplo2
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior = my_list[0]
for i in my_list:
    if i > maior:
        maior = i 
print("maior valor 2:" maior)

#Exemplo3:
ultima_lista - my_list[:]
mel = ultima_lista[0]
for i in ultima_lista[1:]:
    if i > mel:
        mel = if
print("maior valor 3:", mel)


#Encontrar a localizacao de um determinado elemento dentro de uma lista 
frutas = ["abacaxi," "maça", "pera", "mamão", "uva", "melancia"]
elemento = "melancia"
achado = False

for i in range(len(frutas)):
    achado = frutas[i] == elemento 
    if achado:
        break 

if achado == True: 
    print('elemento encontrado no indice: ', i)
else:
    print('não encontrado')
print("")

#Conferir de aposta em loteria
sorteados = [5, 11, 9, 42, 3, 49]
apostados = [3, 7, 11, 42, 34, 49]
acertos = 0

for numero in sorteados:
    if numero in apostados:
        acertos += i

print(acertos)

#Remoçao de numeros repetidos em uma lista
lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("lista original:", lista)

#lista de apoio
vistos = []

#iterar pela lista original de tras para frente 
for i in range(len(lista) -1, -1, -1):
    #se o numero ja esta na lista "vistos", remove-lo da lista original 
    if lista[i] in vistos:
        del listas[i]
else:
    #caso contrario, adicionar a lista "vistos"
    vistos.append(lista[i])    
#Exibir a lista original modificada
print("lista modificada:", lista)


#Listas avançadas
#2D - listas aninhadas bidimensionais
tabela = [[":(", ":)", ":|", ";-;"], [";-;", ":|", ":)", ":("], [":|", ":)", ";-;", ":("]]
print(tabela[0][3])

#3d- matriz tridimensional
cubo = [[[':(', 'y', 'z'],
         [':)', 'y', 'z'],
         [':|', 'y', 'z']],
        [['amor', 'ódio', 'caridade'],
         ['paz', 'esperança', 'férias'],
         ['tina', 'prior', 'pp']],
        [['restinga', 'patrocinio', 'rifaina'],
         ['amazonense', 'fluminense', 'santos'],
         ['pizza', 'lasanha', 'pastel']]]
print(cubo) 
print(cubo[1])
print(cubo[1][0])
print(cubo[1][0][2])

time.sleep(3)


