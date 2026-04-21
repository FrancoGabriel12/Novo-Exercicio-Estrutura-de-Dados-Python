# 1.    Crie uma tupla com 5 números inteiros. Escreva um programa que:
# Imprima o primeiro e o último elemento da tupla.
# Inverta a ordem dos elementos da tupla.
# Verifique se o número 10 está presente na tupla.

# Criando a tupla com 5 números inteiros
numeros = (1, 5, 10, 15, 20)
# Imprimindo o primeiro e o último elemento da tupla
print("Primeiro elemento:", numeros[0])
print("Último elemento:", numeros[-1])
# Invertendo a ordem dos elementos da tupla
numeros_invertidos = numeros[::-1]
print("Tupla invertida:", numeros_invertidos)
# Verificando se o número 10 está presente na tupla
if 10 in numeros:
    print("O número 10 está presente na tupla.")
else:    print("O número 10 não está presente na tupla.")

# 2. Dada a lista [3, 6, 1, 8, 2, 9] , faça as seguintes operações:
# Ordene a lista em ordem crescente.
# Adicione o número 5 na lista.
# Remova o número 1 da lista.
# Inverta a lista.
# Verifique se o número 4 está presente na lista.

# Criando a lista
numeros_lista = [3, 6, 1, 8, 2, 9]
# Ordenando a lista em ordem crescente
numeros_lista.sort()
print("Lista ordenada:", numeros_lista)
# Adicionando o número 5 na lista
numeros_lista.append(5)
print("Lista após adicionar o número 5:", numeros_lista)
# Removendo o número 1 da lista
numeros_lista.remove(1)
print("Lista após remover o número 1:", numeros_lista)
# Invertendo a lista
numeros_lista.reverse()
print("Lista invertida:", numeros_lista)
# Verificando se o número 4 está presente na lista
if 4 in numeros_lista:
    print("O número 4 está presente na lista.")
else:    print("O número 4 não está presente na lista.")

# 3. Dada a tupla (10, 20, 30, 40) , converta-a em uma lista. Adicione os números 50 e 60 à
#lista e depois converta a lista de volta para uma tupla. Imprima o resultado.

# Criando a tupla
tupla = (10, 20, 30, 40)
# Convertendo a tupla em uma lista
lista = list(tupla)
# Adicionando os números 50 e 60 à lista
lista.append(50)
lista.append(60)
# Convertendo a lista de volta para uma tupla
tupla_atualizada = tuple(lista)
print("Tupla atualizada:", tupla_atualizada)


# 4. Crie um dicionário que represente um aluno com as seguintes informações: nome , idade ,
#e notas (uma lista com três notas). Use o nome como chave e as demais informações
#utilize uma estrutura mutável para armazenar. Faça o seguinte:
#Acesse e imprima o nome e a média das notas.
#Adicione uma nova informação curso com o valor "Ciência de Dados" para todos os
#alunos.

# Criando o dicionário do aluno
aluno = {
    "nome": "João",
    "idade": 20,
    "notas": [8.5, 7.0, 9.0]
}
# Acessando e imprimindo o nome e a média das notas
nome = aluno["nome"]
media_notas = sum(aluno["notas"]) / len(aluno["notas"])
print(f"Nome: {nome}, Média das notas: {media_notas:.2f}")
# Adicionando a nova informação curso com o valor "Ciência de Dados"
aluno["curso"] = "Ciência de Dados"
print("Dicionário atualizado do aluno:", aluno)

# 5. Dado os conjuntos A = {1, 2, 3, 4, 5} e B = {4, 5, 6, 7, 8} , faça:
# A união dos dois conjuntos.
#A interseção entre A e B .
#A diferença entre A e B .
#Verifique se o conjunto A é subconjunto de outro conjunto C = {1, 2, 3} .

# Criando os conjuntos A e B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# A união dos dois conjuntos
uniao = A.union(B)
print("União de A e B:", uniao)
# A interseção entre A e B
intersecao = A.intersection(B)
print("Interseção de A e B:", intersecao)
# A diferença entre A e B
diferenca = A.difference(B)
print("Diferença entre A e B:", diferenca)
# Verificando se o conjunto A é subconjunto de outro conjunto C
C = {1, 2, 3}
if A.issubset(C):
    print("O conjunto A é subconjunto do conjunto C.")
else:    print("O conjunto A não é subconjunto do conjunto C.")

#Crie uma lista com os números 1, 2, 2, 3, 4, 4, 4, 5 e:
#Converta a lista em um conjunto para remover os elementos duplicados.
#Converta a lista em uma tupla.

# Criando a lista com números duplicados
numeros_duplicados = [1, 2, 2, 3, 4, 4, 4, 5]
# Convertendo a lista em um conjunto para remover os elementos duplicados
conjunto = set(numeros_duplicados)
print("Conjunto sem elementos duplicados:", conjunto)
# Convertendo a lista em uma tupla
tupla = tuple(numeros_duplicados)
print("Tupla:", tupla)

#Crie um dicionário para armazenar os preços de produtos: {'arroz': 5.00, 'feijão':
#7.50, 'batata': 2.50} . Escreva um programa que:
#Itere sobre o dicionário e imprima o nome de cada produto e seu preço.
#Adicione um novo produto ao dicionário ( macarrão , R$ 3.20).
#Verifique se existe um produto chamado açúcar no dicionário.

# Criando o dicionário de preços dos produtos
precos = {'arroz': 5.00, 'feijão': 7.50, 'batata': 2.50}
# Iterando sobre o dicionário e imprimindo o nome de cada produto e seu preço
for produto, preco in precos.items(): # Imprime o nome do produto e seu preço formatado com duas casas decimais 
    print(f"Produto: {produto}, Preço: R$ {preco:.2f}")
# Adicionando um novo produto ao dicionário
precos['macarrão'] = 3.20
print("Dicionário atualizado de preços:", precos)
# Verificando se existe um produto chamado açúcar no dicionário
if 'açúcar' in precos:
    print("O produto 'açúcar' existe no dicionário.")
else:
    print("O produto 'açúcar' não existe no dicionário.")

#Crie uma função que receba uma tupla de três elementos (nome, idade, cidade) e
#desempacote esses valores para imprimir uma frase como: "João, 30 anos, mora em
#São Paulo." . Teste a função com diferentes tuplas.

def imprimir_informacoes(tupla):
    nome, idade, cidade = tupla
    print(f"{nome}, {idade} anos, mora em {cidade}.")
# Testando a função com diferentes tuplas
imprimir_informacoes(("João", 30, "São Paulo"))
imprimir_informacoes(("Maria", 25, "Rio de Janeiro"))
imprimir_informacoes(("Carlos", 40, "Belo Horizonte"))

#Escreva uma função que receba duas listas de números. A função deve:
#Retornar um conjunto com os elementos que estão presentes em ambas as listas.
#Retornar uma lista com todos os elementos das duas listas, sem repetição.
#Retornar a concatenação das duas listas.

def processar_listas(lista1, lista2):
    # Retornar um conjunto com os elementos que estão presentes em ambas as listas
    conjunto_comum = set(lista1).intersection(set(lista2))
    # Retornar uma lista com todos os elementos das duas listas, sem repetição
    lista_unica = list(set(lista1).union(set(lista2)))
    # Retornar a concatenação das duas listas
    lista_concatenada = lista1 + lista2
    return conjunto_comum, lista_unica, lista_concatenada
# Testando a função com diferentes listas
lista_a = [1, 2, 3, 4]
lista_b = [3, 4, 5, 6]
conjunto_comum, lista_unica, lista_concatenada = processar_listas(lista_a, lista_b)
print("Conjunto com elementos comuns:", conjunto_comum)
print("Lista com todos os elementos sem repetição:", lista_unica)
print("Concatenação das duas listas:", lista_concatenada)

#Crie uma classe Turma que armazena o nome da turma e um dicionário com os alunos,
#onde a chave é o nome do aluno e o valor é uma lista de três notas.
#Implemente um método adicionar_aluno(nome, notas) que adiciona um aluno ao
#dicionário.
#Implemente um método calcular_media(nome) que calcula e retorna a média das
#notas de um aluno.
#Implemente um método imprimir_turma() que imprime o nome da turma e os
#alunos com suas respectivas médias.

class Turma:
    def __init__(self):
        self.nome_turma = ""
        self.alunos = {}
    def adicionar_aluno(self, nome, notas):
        self.alunos[nome] = notas
    def calcular_media(self, nome):
        if nome in self.alunos: # Verifica se o aluno existe no dicionário
            notas = self.alunos[nome] # Obtém as notas do aluno
            media = sum(notas) / len(notas)
            return media
        else:
            return None # Retorna None se o aluno não existir
    def imprimir_turma(self):
        print(f"Turma: {self.nome_turma}")
        for nome, notas in self.alunos.items():
            media = self.calcular_media(nome)
            print(f"Aluno: {nome}, Media: {media: .2f}")

# Testando a classe Turma
turma = Turma()
turma.nome_turma = "Turma A" # Definindo o nome da turma
turma.adicionar_aluno("João", [8.5, 7.0, 9.0]) # Adicionando alunos e suas notas
turma.adicionar_aluno("Maria", [9.0, 8.5, 7.5])
turma.adicionar_aluno("Carlos", [7.0, 6.5, 8.0])
turma.imprimir_turma() # Imprimindo as informações da turma e dos alunos 

#Dada a classe turma, criada anteriormente, implemente um dicionário que armazene várias
#turmas. Cada turma é identificada por um código inteiro.
#Adicione uma nova turma ao dicionário.
#Adicione um aluno a uma turma existente.
#Imprima todas as turmas e seus alunos com suas respectivas médias.

class Turma:
    def __init__(self):
        self.nome_turma = ""
        self.alunos = {}
    def adicionar_aluno(self, nome, notas):
        self.alunos[nome] = notas
    def calcular_media(self, nome):
        if nome in self.alunos:
            notas = self.alunos[nome]
            media = sum(notas) / len(notas)
            return media
        else:
            return None
    def imprimir_turma(self):
        print(f"Turma: {self.nome_turma}")
        for nome, notas in self.alunos.items():
            media = self.calcular_media(nome)
            print(f"Aluno: {nome}, Media: {media: .2f}")
# Criando um dicionário para armazenar várias turmas
turmas = {}
# Adicionando uma nova turma ao dicionário
turma_a = Turma() # Criando uma nova turma
turma_a.nome_turma = "Turma A" # Definindo o nome da turma
turmas[1] = turma_a # Adicionando a turma ao dicionário com um código inteiro

# Adicionando outra turma ao dicionário
turma_b = Turma() # Criando outra turma
turma_b.nome_turma = "Turma B" # Definindo o nome da turma
turmas[2] = turma_b # Adicionando a turma ao dicionário com um código inteiro

# Adicionando um aluno a uma turma existente
turmas[1].adicionar_aluno("João", [8.5, 7.0, 9.0]) # Adicionando um aluno à turma A
# Imprimindo todas as turmas e seus alunos com suas respectivas médias
for codigo, turma in turmas.items():
    print(f"Código da Turma: {codigo}")
    turma.imprimir_turma()

turmas[2].adicionar_aluno("Maria", [9.0, 8.5, 7.5]) # Adicionando um aluno à turma B
for codigo, turma in turmas.items():
    print(f"Código da Turma: {codigo}")
    turma.imprimir_turma()


