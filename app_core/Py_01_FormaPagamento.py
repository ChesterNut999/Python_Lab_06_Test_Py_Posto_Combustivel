# MÓDULO 1 - SELECIONAR E VALIDAR MEIOS DE PAGAMENTO

# BLOCO 1 - ESCOLHA E VALIDAÇÃO DO MEIO DE PAGAMENTO
entrada = None
bandeira = None
notas = None

print('\nSEJA BEM VINDO AO POSTO DE COMBUSTÍVEL')

while True:
    lista_entrada = ["", "Cartão", "Dinheiro", "QR Code"]

    try:
        print('\n---------- MENU PRINCIPAL ----------')

        entrada = int(input('\nESCOLHA UMA FORMA DE PAGAMENTO:\n'
                            '1 - para ' + lista_entrada[1] + ' (MasterCard ou Visa)\n'
                            '2 - para ' + lista_entrada[2] + '\n'
                            '3 - para ' + lista_entrada[3] + '\n'
                            'DIGITE A OPÇÃO DESEJADA: '))

        print('\n' + ('-' * 60) + '\n' + lista_entrada[entrada].upper() + ' SELECIONADO!\n'
               'Aguarde, processando...\n' + ('-' * 60))

        # SE CARTÃO, ESCOLHE BANDEIRA
        if entrada == 1:
            while True:
                try:
                    lista_bandeira = ["Voltar", "MasterCard", "Visa"]

                    bandeira = int(input('\nESCOLHA A BANDEIRA DO CARTÃO:\n'
                                         '1 - para ' + lista_bandeira[1] + '\n'
                                         '2 - para ' + lista_bandeira[2] + '\n'
                                         '0 -- para ' + lista_bandeira[0] + ' ao menu inicial\n'
                                         'DIGITE A OPÇÃO DESEJADA: '))

                    if bandeira == 1 or bandeira == 2:
                        print('\n' + ('-' * 60) + '\n' + lista_bandeira[bandeira].upper() + '. BANDEIRA SELECIONADA!\n'
                              'Aguarde, processando...\n' + ('-' * 60))
                        break

                    if bandeira == 0:
                        print('\n' + ('-' * 60) + '\n' + lista_bandeira[bandeira].upper() + ' AO MENU INICIAL SELECIONADO!\n'
                              'Aguarde, processando...\n' + ('-' * 60))

                        break

                    else:
                        print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
                        continue

                except BaseException:
                    print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
                    continue

        # SE DINHEIRO, PROSSEGUE OU NÃO
        elif entrada == 2:
            while True:
                try:
                    lista_opcoes = ["Voltar", "Sim", 20, 50, 100]

                    notas = int(input('\n====> N Ã O  H Á  T R O C O <====\n'
                                      'INSIRA SOMENTE NOTAS DE: R$' + str(int(lista_opcoes[2])) + ', R$' + str(int(lista_opcoes[3])) + ', R$' + str(int(lista_opcoes[4])) + '\n' +
                                      '\nDESEJA PROSSEGUIR?\n'
                                      '1 - para ' + lista_opcoes[1] + '\n'
                                      '0 -- para ' + lista_opcoes[0] + ' ao menu inicial\n'
                                      'DIGITE A OPÇÃO DESEJADA: '))

                    if notas == 1:
                        print('\n' + ('-' * 60) + '\n' + lista_opcoes[notas].upper() + ' SELECIONADO!\n'
                              'Aguarde, processando...\n' + ('-' * 60))
                        break

                    elif notas == 0:
                        print('\n' + ('-' * 60) + '\n' + lista_opcoes[notas].upper() + ' AO MENU INICIAL SELECIONADO!\n'
                              'Aguarde, processando...\n' + ('-' * 60))
                        break

                    else:
                        print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
                        continue

                except BaseException:
                    print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
                    continue

        # SE QR Code, GERA E VALIDA
        elif entrada == 3:
            while entrada == 3:
                break

        else:
            print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
            continue

        break

    except BaseException:
        print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
        continue

