print('''
        Exercício 3.1 - Pense Python
        15/08/2022 - Grupo de Estudos PyLadies
        Coloque a última letra de uma palavra na coluna 70
        ''')
      
input_palavra = input('Informe a palavra que será justificada a esquerda: ')

def justifique_direita(palavra):
    espaços_total = 70
    quantidade_letras = len(palavra)
    espaços_esquerda = espaços_total - quantidade_letras
    print(espaços_esquerda * ' ' + palavra)
    
justifique_direita(input_palavra)
    
