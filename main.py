import datetime
import secrets

from entities.Fruta import Fruta
from entities.Legume import Legume
from entities.Verdura import Verdura
from services.Carrinho import Carrinho

def main():

    frutas = []
    nome_frutas = ["abacaxi", "maçã\t", "banana\t", "melão\t", "laranja", "limão\t", "uva\t\t", "goiaba\t", "mamão\t", "pêra"]
    codigo_frutas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    quantidade_frutas = [60, 70, 85, 90, 120, 115, 170, 100, 40, 50]
    preco_frutas = [5.00, 1.00, 0.50, 6.00, 1.50, 1.20, 0.80, 3.50, 9.00, 4.00]

    frutas.append(Fruta(nome_frutas, codigo_frutas, quantidade_frutas, preco_frutas))

    legumes = []
    nome_legumes= ["cenoura", "abóbora", "batata\t", "jiló\t", "beterraba", "ervilha", "inhame\t", "aipim\t", "palmito", "nabo\t"]
    codigo_legumes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    quantidade_legumes = [30, 45, 60, 50, 32, 30, 28, 70, 80, 20]
    preco_legumes = [4.50, 3.00, 6.00, 6.50, 3.00, 7.00, 2.50, 8.00, 7.50, 6.00]

    legumes.append(Legume(nome_legumes, codigo_legumes, quantidade_legumes, preco_legumes))

    verduras = []

    nome_verduras = ["acelga\t", "alface\t", "agrião\t", "rúcula\t", "couve\t", "salsa\t", "espinafre", "hortelã", "repolho", "coentro"]
    codigo_verduras = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    quantidade_verduras = [20, 25, 30, 32, 20, 16, 18, 24, 30, 10]
    preco_verduras = [1.50, 3.50, 4.60, 3.40, 4.90, 7.80, 5.60, 3.00, 4.50, 1.00]

    verduras.append(Verdura(nome_verduras, codigo_verduras, quantidade_verduras, preco_verduras))

    j = 0
    p = 0
    q = 0
    frutas_compradas = []
    legumes_comprados = []
    verduras_compradas = []
    mercadorias_compradas = []



    print("***************************************************\n")
    print("Bem-vindo(a) ao Império do Horti-frutti\n")
    print("Vamos iniciar a compra!\n")
    print("***************************************************\n")

    print("\nIniciando pelas frutas.\n")

    print("Tabela das frutas:\n")
    print("Descrição\tcódigo\testoque\tpreço(R$)\n")
    for i in range(0, 10):
        print(nome_frutas[i], '\t', codigo_frutas[i], '\t\t', quantidade_frutas[i], '\t', preco_frutas[i], '\n')

    numero = int(input("Digite a quantidade de frutas que desejas:\n"))

    while j < numero:

        codigo = int(input("Digite o código da fruta que desejas:\n"))
        cod_encontrado = False

        for i in range(0, 10):
            if codigo == codigo_frutas[i]:
                quanti = int(input(f"Qual a quantidade de {nome_frutas[i]}?"))

                if quanti <= quantidade_frutas[i]:
                    print(f"{quanti} {nome_frutas[i]}(s) adicionado(a)(s) com sucesso ao carrinho.\n")
                    Carrinho.adicionaMercadoria(nome_frutas[i])
                    quantidade_frutas[i] -= quanti
                    frutas_compradas.append((nome_frutas[i], quanti, preco_frutas[i]))
                else:
                    print(
                        "Quantidade solicitada impossível de ser atendida, pois o estoque desse produto é insuficiente.\n")
                cod_encontrado = True
                break
        if not cod_encontrado:
            print("Código inexistente!\n")
        j += 1

    print("**************MEMORANDO PARCIAL***************\n")
    print("Descrição\tQuantidade\tPreço unitário\tPreço parcial\n")

    total_frutas = 0.0

    for fruta in frutas_compradas:
        nome, quantidade, preco_unitario = fruta
        total_item = quantidade * preco_unitario
        total_frutas += total_item
        print(f"{nome}\t\t\t{quantidade}\t\t{preco_unitario:.2f}\t\t{total_item:.2f}")

    print(f"Total a pagar por frutas: R${total_frutas:.2f}\n")


    print("\nIndo para os legumes:\n")
    print("Tabela dos legumes:\n")
    print("Descrição\tcódigo\testoque\tpreço(R$)\n")
    for i in range(0, 10):
        print(nome_legumes[i], '\t', codigo_legumes[i], '\t\t', quantidade_legumes[i], '\t', preco_legumes[i], '\n')


    numero1 = int(input("Digite a quantidade de legumes que desejas:\n"))
    cod1_encontrado = False

    while p < numero1:
        codigo1 = int(input("Digite o código do legume que desejas:\n"))

        for i in range(0, 10):

            if codigo1 == codigo_legumes[i]:
                quanti1 = int(input(f"Qual a quantidade de {nome_legumes[i]}?"))

                if quanti1 <= quantidade_frutas[i]:
                    print(f"{quanti1}  {nome_legumes[i]} (s) adicionado(a) com sucesso ao carrinho.\n")
                    Carrinho.adicionaMercadoria(nome_legumes[i])
                    legumes_comprados.append((nome_legumes[i], quanti1, preco_legumes[i]))

                    quantidade_legumes[i] -= quanti1
                else:
                    print(
                        "Quantidade solicitada impossível de ser atendida, pois o estoque desse produto é insuficiente.\n")
                cod1_encontrado = True
                break
        if not cod1_encontrado:
            print("Código inexistente!\n")
        p += 1


    print("**************MEMORANDO PARCIAL***************\n")
    print("Descrição\tQuantidade\tPreço unitário\tPreço parcial\n")

    total_legumes = 0.0

    for legume in legumes_comprados:
        nome1, quantidade1, preco_unitario1 = legume
        total_item1 = quantidade1 * preco_unitario1
        total_legumes += total_item1
        print(f"{nome1}\t{quantidade1}\t\t{preco_unitario1:.2f}\t\t{total_item1:.2f}")

    print(f"\nTotal a pagar por esses legumes: R${total_legumes:.2f}\n")

    print("\nIndo para as verduras:\n")
    print("Tabela das verduras:\n")
    print("Descrição\tcódigo\testoque\tpreço(R$)\n")
    for i in range(0, 10):
        print(nome_verduras[i], '\t', codigo_verduras[i], '\t\t', quantidade_verduras[i], '\t', preco_verduras[i], '\n')


    numero2 = int(input("Digite a quantidade de verduras que desejas comprar:\n"))

    while q < numero2:
        codigo2 = int(input("Digite o código da verdura que desejas:\n"))
        cod2_encontrado = False

        for i in range(0, 10):
            if codigo2 == codigo_verduras[i]:
                quanti2 = int(input(f"Qual a quantidade de {nome_verduras[i]}?"))

                if quanti2 <= quantidade_verduras[i]:
                    print(f"{quanti2}  {nome_verduras[i]} (s) adicionado(a) com sucesso ao carrinho.\n")
                    Carrinho.adicionaMercadoria(nome_verduras[i])
                    verduras_compradas.append((nome_verduras[i], quanti2, preco_verduras[i]))

                    quantidade_verduras[i] -= quanti2
                else:
                    print("Quantidade solicitada impossível de ser atendida, pois o estoque desse produto é insuficiente.\n")
                cod2_encontrado = True
                break
        if not cod2_encontrado:
            print("Código inexistente!\n")
        q += 1

    print("**************MEMORANDO PARCIAL***************\n")
    print("Descrição\tQuantidade\tPreço unitário\tPreço parcial\n")

    total_verduras = 0.0

    for verdura in verduras_compradas:
        nome2, quantidade2, preco_unitario2 = verdura
        total_item2 = quantidade2* preco_unitario2
        total_verduras += total_item2
        print(f"{nome2}\t\t{quantidade2}\t\t{preco_unitario2:.2f}\t\t{total_item2:.2f}")

    print(f"\nTotal a pagar por essas verduras: R${total_verduras:.2f}\n")

    total_final = total_frutas + total_legumes + total_verduras
    mercadorias_compradas.append((frutas_compradas, legumes_comprados, verduras_compradas))

    print("***********COMPROVANTE DE COMPRA********************\n")

    print("Descição\tquantidade\tpreço unitário\tpreço parcial\n")
    for fruta in frutas_compradas:
        nome, quantidade, preco_unitario = fruta
        total_item = quantidade * preco_unitario
        print(f"{nome}\t\t\t{quantidade}\t\t{preco_unitario:.2f}\t\t{total_item:.2f}")

    for legume in legumes_comprados:
        nome1, quantidade1, preco_unitario1 = legume
        total_item1 = quantidade1 * preco_unitario1
        print(f"{nome1}\t\t\t{quantidade1}\t\t{preco_unitario1:.2f}\t\t{total_item1:.2f}")

    for verdura in verduras_compradas:
        nome2, quantidade2, preco_unitario2 = verdura
        total_item2 = quantidade2 * preco_unitario2
        print(f"{nome2}\t\t{quantidade2}\t\t\t{preco_unitario2:.2f}\t\t{total_item2:.2f}")

    print(f"\nPreço a pagar pela compra: R$ {total_final:.2f}\n")

    print("Compra finalizada com sucesso!\n")

    hora_atual = datetime.datetime.now()
    print("Data e hora da impressão de comprovante: ", hora_atual)
    numero_aleatorio = secrets.randbelow(10000000000)
    print("ID do comprovante: ", numero_aleatorio)
    print("\nOBRIGADO POR ESCOLHER O IMPÉRIO DO HORTI-FRUTTI\n")




if __name__ == "__main__":
    main()

