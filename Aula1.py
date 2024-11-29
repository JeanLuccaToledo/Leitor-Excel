nome =  input("Nome Usuário: ") #Input ele permite que o programa pause e aguarde o usuário digitar algo no console, retornando o texto inserido como uma string.
idade = int(input("Idade Usuário: "))

print(f"Voce tem {idade} anos")
print(f"E seu nome é {nome}")

#format() # Organiza na Ordem.
mensagem = f"Meu nome é {nome} e tenho {idade} anos.".format(nome, idade)
print(mensagem)
# Saída: Meu nome é Jean e tenho 22 anos.


#type retorna o tipo da variavel
x = 2
print(type(x))
Pessoa = type('Pessoa', (object,), {'Nome': 'Gabriel', 'Idade': 22})

# Instanciando a classe
p = Pessoa()
print(p.nome)  # Saída: Gabriel
print(p.idade)  # Saída: 22