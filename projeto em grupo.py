#Ana Paula, Lohran e Matheus A.
#Atendimento de uma clinica de estetica denominada Beauty Body.

def valor(x):
  """função que observa se o valor de entrada é valido"""
  if (x <= 5) and (x > 0):
    return x
  else:
    print('Valor de entrada não aceito. Escolha uma das opções (de 1 a 5).')
    x = int(input("Diga a opção que deseja escolher: \n"))
    return x



print('Boas vindas, eu sou a Pri, sua atendente virtual da clínica de estética Beauty Body. \n')
usuarios = []
cont = 'sim'
hr = [['segunda - 9 horas'], ['segunda - 13 horas'], ['segunda - 15 horas']]
nome = input('Como nós podemos te chamar? (Opcional)\n')
num_contat = input('\nNos dê um telefone para contato - com ddd: (Opcional)\n')

while (cont == 'sim') or (cont == 'SIM') or (cont == 'Sim') or (cont == 's'):
    infos = []
    print('\nComo podemos te ajudar? \n1 - Serviços oferecidos. \n2 - Promoções. \n3 - Horários disponíveis. \n4 - Atendimento com atendente. \n5 - Sair.\n')
    print('\n')
    opcao = valor(int(input('Digite o número relacionado com o seu desejo: \n')))
    #criar função que verifica se o valor digitado está entre 1 e 5.
    print('\n')
    list.append(infos, nome)
    list.append(infos, num_contat)

#entra na primeira opção:
    if (opcao == 1):
        print('Serviços oferecidos: \n1 - Limpeza de pele. \n2 - Drenagem linfática. \n3 - Massagem corporal. \n4 - Esfoliação corporal. \n5 - Sugestões.\n')
        serv = int(input('\nQual o serviço deseja consultar? (digite o número correspondente)\n'))
        
        if (serv == 1):
            print('\nLimpeza de pele: \nValor: R$ 60,00 \nHorários: segunda a sexta de 09h às 17h')
            opcao = ['serviços oferecidos']
            list.append(infos, opcao)
        elif (serv == 2):
            print('\nDrenagem linfática: \nValor: R$ 120,00 por seção \nHorários: segunda a sexta de 09h às 17h')
            opcao = ['serviços oferecidos']
            list.append(infos, opcao)
        elif (serv == 3):
            print('\nMassagem corporal: \nValor: R$ 80,00 \nHorários: segunda a sexta de 09h às 17h')
            opcao = ['serviços oferecidos']
            list.append(infos, opcao)
        elif (serv == 4):
            print('\nEsfoliação corporal: \nValor: R$ 45,00 \nHorários: segunda a sexta de 09h às 17h')
            opcao = ['serviços oferecidos']
            list.append(infos, opcao)
        else:
            nv_duvida = input('\nDiga qual a sua sugestão: \n')
            opcao = ['serviços oferecidos']
            list.append(infos, opcao)
            list.append(infos, ['sugestão'])
            list.append(infos, nv_duvida)

            
#entra na segunda opção:
    elif (opcao == 2):
        print('Promoções disponíveis: \n1 - Promoção de limpeza de pele + esfoliação corporal. \n2 - Promoção limpeza de pele + massagem corporal + esfoliação. \n3 - Promoção de drenagem linfática.\n')
        consulta = int(input('\nQual promoção deseja consultar? (digite o número correspondente)\n'))
        if (consulta == 1):
            print('\nPromoção válida para mulheres com mais de 30 anos.')
            print('Valor: R$ 95,00')
        elif (consulta == 2):
            print('\nPromoção válida para o público com mais de 18 anos.')
            print('Valor: R$ 175,00')
        elif (consulta == 3):
            print('\nPacote de drenagem linfática: 5 seções.')
            print('Valor: R$ 550,00')
        opcao = ['promoções disponíveis']
        list.append(infos, opcao)
        
    
#entra na terceira opção:
    elif (opcao == 3):
        print('Horários disponíveis no dia: \n')
        print(hr)
        i = int(input('\nDiga qual o horário deseja reservar: (ex. primeiro hórario oferecido: digite 1)\n'))
        j = input('\nDiga qual o procedimento que deseja realizar: \n\n')
        if (i == 1):
            print('\nHorário selecionado:') 
            sel = list.pop(hr[i-1])
            print(sel)
        elif (i == 2):
            print('\nHorário selecionado:')
            sel = list.pop(hr[i-1])
            print(sel)
        elif (i == 3):
            print('\nHorário selecionado:')
            sel = list.pop(hr[i-1])
            print(sel)
        opcao = ['horários disponíveis']
        list.append(infos, opcao)
        list.append(infos, j)
        list.append(infos, sel)
            
    

#entra na quarta opção:
    elif (opcao == 4):
        print('\nPara entrar em contato com nossos atendentes, ligue para a nossa central de atendimento: \nXXX-XXX-XXX')
        opcao = ['atendimento com atendente']
        list.append(infos, opcao)

    
    
#encerra o atendimento:
    else:
        print('Atendimento finalizado.\nA clínica Beauty Body agradece pela preferência. ')
        break
    list.append(usuarios, infos)
    cont = input('\nDeseja fazer outra operação?\n')



def imprime(lista):
  """imprime linha a linha da lista"""
  for i in lista:
    print(i)

#imprime(usuarios)
#vai imprimir o usuário e suas ações.
