#Ana Paula, Lohran e Matheus A.
#Atendimento de uma clinica de estetica denominada Beauty Body.



#Função para observar se os valores dados são aceitos
def valor(x):
  """função que observa se o valor de entrada é valido"""
  if (x <= 6) and (x > 0):
    return x
  else:
    print('Valor de entrada não aceito. Escolha uma das opções (de 1 a 6).')
    x = int(input("Diga a opção que deseja escolher: \n"))
    return x



print('Boas vindas, eu sou a Pri, sua atendente virtual da clínica de estética Beauty Body. \n')
usuarios = [] #lista com as informações de todos os usuários, bem como suas pesquisas ou ações no atendimento.
cont = 'sim' #variavel para continuar rodando o looping while.
hr_lp = [['segunda - 9 horas'], ['segunda - 13 horas'], ['segunda - 15 horas']] #horarios limpeza de pele.
hr_mc = [['segunda - 9 horas'], ['segunda - 13 horas'], ['segunda - 15 horas']] #horarios massagem coporal.
hr_ec = [['segunda - 9 horas'], ['segunda - 13 horas'], ['segunda - 15 horas']] #horarios esfoliação corporal.
hr_dl = [['segunda - 9 horas'], ['segunda - 13 horas'], ['segunda - 15 horas']] #horarios drenagem linfática..

nome = input('Como nós podemos te chamar? (Opcional)\n')
num_contat = input('\nNos dê um telefone para contato - com ddd: (Opcional)\n')

while (cont == 'sim') or (cont == 'SIM') or (cont == 'Sim') or (cont == 's') or (cont == 'S'):
    infos = [] #lista com as informações de cada ação do usuário
    print('\nComo podemos te ajudar? \n1 - Serviços oferecidos. \n2 - Promoções. \n3 - Horários disponíveis. \n4 - Atendimento com atendente. \n5 - Sugestão de melhorias ou Reclmações.\n6 - Sair.\n')
    print('\n')
    opcao = valor(int(input('Digite o número relacionado com o seu desejo: \n')))
    print('\n')
    list.append(infos, nome)
    list.append(infos, num_contat)
    #adiciona o nome e o número na lista de infos do usuario

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
            #adiciona a opção selecionada e a ação do usuário na lista infos.

            
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
        #adiciona a opção selecionada e a ação do usuário na lista infos.
        
    
#entra na terceira opção:
    elif (opcao == 3):
        print('\nProcedimentos: \n1 - Limpeza de pele. \n2 - Massagem Corporal. \n3 - Esfoliação corporal. \n4 - Drenagem linfática. \n')
        j = int(input('\nDiga qual o procedimento que deseja consultar os horários disponíveis: \n\n'))
        
        if (j == 1): #Limpesa de pele
          opcao = ['horário marcado - limpeza de pele']
          print('\nHorários disponíveis para limpeza de pele:\n')
          print(hr_lp)
          print('\n')
          i = int(input('\nDiga qual o horário deseja reservar: (ex. primeiro hórario oferecido: digite 1)\n'))
          if (i == 1):
            print('\nHorário selecionado:') 
            sel = list.pop(hr_lp[i-1])
            print(sel)
          elif (i == 2):
            print('\nHorário selecionado:')
            sel = list.pop(hr_lp[i-1])
            print(sel)
          elif (i == 3):
            print('\nHorário selecionado:')
            sel = list.pop(hr_lp[i-1])
            print(sel)

        elif (j == 2): #Massagem corporal
          opcao = ['horário marcado - massagem corporal']
          print('\nHorários disponíveis para massagem corporal:\n')
          print(hr_mc)
          print('\n')
          i = int(input('\nDiga qual o horário deseja reservar: (ex. primeiro hórario oferecido: digite 1)\n'))
          if (i == 1):
            print('\nHorário selecionado:') 
            sel = list.pop(hr_mc[i-1])
            print(sel)
          elif (i == 2):
            print('\nHorário selecionado:')
            sel = list.pop(hr_mc[i-1])
            print(sel)
          elif (i == 3):
            print('\nHorário selecionado:')
            sel = list.pop(hr_mc[i-1])
            print(sel)


        elif (j == 3): #Esfoliação corporal
          opcao = ['horário marcado - esfoliação corporal']
          print('\nHorários disponíveis para esfoliação corporal:\n')
          print(hr_ec)
          print('\n')
          i = int(input('\nDiga qual o horário deseja reservar: (ex. primeiro hórario oferecido: digite 1)\n'))
          if (i == 1):
            print('\nHorário selecionado:') 
            sel = list.pop(hr_ec[i-1])
            print(sel)
          elif (i == 2):
            print('\nHorário selecionado:')
            sel = list.pop(hr_ec[i-1])
            print(sel)
          elif (i == 3):
            print('\nHorário selecionado:')
            sel = list.pop(hr_ec[i-1])
            print(sel)  

        
        elif (j == 4): #Drenagem linfática
          opcao = ['horário marcado - drenagem linfática']
          print('\nHorários disponíveis para drenagem linfática:\n')
          print(hr_dl)
          print('\n')
          i = int(input('\nDiga qual o horário deseja reservar: (ex. primeiro hórario oferecido: digite 1)\n'))
          if (i == 1):
            print('\nHorário selecionado:') 
            sel = list.pop(hr_dl[i-1])
            print(sel)
          elif (i == 2):
            print('\nHorário selecionado:')
            sel = list.pop(hr_dl[i-1])
            print(sel)
          elif (i == 3):
            print('\nHorário selecionado:')
            sel = list.pop(hr_dl[i-1])
            print(sel)

        list.append(infos, opcao)
        #list.append(infos, j)
        list.append(infos, sel)
        #adiciona a opção selecionada e a ação do usuário na lista infos.
            
    

#entra na quarta opção:
    elif (opcao == 4):
        print('\nPara entrar em contato com nossos atendentes, ligue para a nossa central de atendimento: \nXXX-XXX-XXX')
        opcao = ['atendimento com atendente']
        list.append(infos, opcao)
        #adiciona a opção selecionada e a ação do usuário na lista infos.



#entra na quinta opção:
    elif (opcao == 5):
        print('\n1 - Sugestão de melhorias. \n2 - Reclamação.\n')
        q = int(input('\nDiga qual das operações deseja realizar: (Diga o número correspondente) \n'))
        if (q == 1):
            m = input('\nNos diga em que podemos melhorar: \n')
            opcao = ['sugestão de melhoria']
            list.append(infos, opcao)
            list.append(infos, m)
        elif (q == 2):
            r = input('\nQual a sua reclamação?\n')
            opcao = ['reclamação']
            list.append(infos, opcao)
            list.append(infos, r)
            #adiciona a opção selecionada e a ação do usuário na lista infos.
        
    


#encerra o atendimento:
    else:
        break
    list.append(usuarios, infos)
    #adiciona os dados armazenados na lista infos dentro da lista de informações registradas pelos usuários.
    cont = input('\nDeseja fazer outra operação?\n')
print('\n')
print('Atendimento finalizado.\nA clínica Beauty Body agradece pela preferência. ')




#imprime os dados e operações dos usuários:
def imprime(lista):
  """imprime cada linha da lista"""
  for i in lista:
    print(i)

#imprime(usuarios)
#vai imprimir o usuário e suas ações.
