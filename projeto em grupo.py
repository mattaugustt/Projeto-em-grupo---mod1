#Matheus Augusto

#atendimento automatizado de duvidas sobre a empresa
# -> criar 'duvidas frequentes' e criar uma variavel para inserir
#outras duvidas.


print('Olá, eu sou o X, o seu atendente virtual. \nComo posso te ajudar?\n')
novas_duvidas = []
numeros = []
nomes = []
cont = 'sim'

while (cont == 'sim'):
    print('1 - Duvidas frequentes. \n2 - Consultas. \n3 - Informações. \n4 - Atendimento com atendente. \n5 - Sair.\n')
    print('\n')
    opcao = int(input('Digite o número relacionado com o seu desejo: \n'))
    print('\n')

    if (opcao == 1):
        print('Duvidas frequentes: \n1 - Duvida n° 1; \n2 - Duvida n° 2; \n3 - Duvida n° 3; \n4 - Outra duvida.\n')
        duvida = int(input('Diga qual a sua duvida? (digite o número correspondente)\n'))
        if (duvida == 1):
            print('Resposta da 1a duvida')
        elif (duvida == 2):
            print('Resposta da 2a duvida')
        elif (duvida == 3):
            print('Resposta da 3a duvida')
        else:
            nv_duvida = input('Diga qual a sua duvida: \n')
            nome = input('Nos diga seu nome:\n')
            num_contat = input('Nos dê um telefone para contato (com ddd):\n')
            list.append(nomes, nome)
            list.append(novas_duvidas, nv_duvida)
            list.append(numeros, num_contat)
            
    elif (opcao == 2):
        print('Consultas: \n1 - Consulta n° 1; \n2 - Consulta n° 2; \n3 - Consulta n° 3.\n')
        consulta = int(input('O que deseja consultar? (digite o número correspondente)\n'))
        if (consulta == 1):
            print('Resposta da 1a consulta')
        elif (consulta == 2):
            print('Resposta da 2a consulta')
        elif (consulta == 3):
            print('Resposta da 3a consulta')
        
    elif (opcao == 3):
        print('Informações: \n1 - Informação n° 1; \n2 - Informação n° 2; \n3 - Informação n° 3.\n')
        info = int(input('Diga qual a informação que deseja obter: (digite o número correspondente)\n'))
        if (consulta == 1):
            print('Primeira informação.')
        elif (consulta == 2):
            print('Segunda informação.')
        elif (consulta == 3):
            print('Terceira informação.')
            
    elif (opcao == 4):
        print('Para entrar em contato com nossos atendentes, ligue para o nosso SAC: \nXXX-XXX-XXX')

    else:
        break
       
    cont = input('\nDeseja fazer outra operação?\n')
