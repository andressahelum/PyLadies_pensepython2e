# Lenght
# Vendo na prática funções imbutidas no python x funções criadas

input_palavra = input('Digite uma palavra: ')

# Função própria do python
print(f'A quantidade de letras em {input_palavra} é {len(input_palavra)}.')

# Função escrita manualmente
def tamanho_string(palavra):
    quantidade_letras = 0
    for letra in palavra:
        quantidade_letras += 1
    print(f'A quantidade de letras em {palavra} é {quantidade_letras}.')

tamanho_string(input_palavra)
    
