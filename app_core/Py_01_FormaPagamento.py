# MÓDULO 1 - SELECIONAR E VALIDAR MEIOS DE PAGAMENTO
import runpy
from app_core import Py_02_Qtd_Tipo_Combustivel

# BLOCO 1 - ESCOLHA E VALIDAÇÃO DO MEIO DE PAGAMENTO
print('\nSEJA BEM VINDO AO POSTO DE COMBUSTÍVEL')

while True:
    try:
        print('\n---------- MENU PRINCIPAL ----------')

        lista_entrada = ["sair", "cartão", "dinheiro", "QR Code"]

        entrada = int(input('\nESCOLHA UMA FORMA DE PAGAMENTO:\n'
                            '1 - para ' + lista_entrada[1] + ' (MasterCard ou Visa)\n'
                            '2 - para ' + lista_entrada[2] + '\n'
                            '3 - para ' + lista_entrada[3] + '\n'
                            '0 ** para ' + lista_entrada[0] + ' deste terminal\n'
                            'DIGITE A OPÇÃO DESEJADA: '))

        print('\n' + ('-' * 60) + '\n' + lista_entrada[entrada].upper() + ' SELECIONADO!\n'
               'Aguarde, processando...\n' + ('-' * 60))

        # SE CARTÃO, ESCOLHE BANDEIRA
        if entrada == 1:
            try:
                lista_bandeira = ["voltar ao menu inicial", "MasterCard", "Visa"]

                bandeira = int(input('\nESCOLHA A BANDEIRA DO CARTÃO:\n'
                                     '1 - para ' + lista_bandeira[1] + '\n'
                                     '2 - para ' + lista_bandeira[2] + '\n'
                                     '0 ** para ' + lista_bandeira[0] + '\n'
                                     'DIGITE A OPÇÃO DESEJADA: '))

                if bandeira == 1 and entrada == 1 or bandeira == 2 and entrada == 1:
                    print('\n' + ('-' * 60) + '\n' + lista_bandeira[bandeira].upper() + '. BANDEIRA SELECIONADA!\n'
                          'Aguarde, processando...\n' + ('-' * 60))
                    break

                if bandeira == 0 and entrada == 1:
                    print('\n' + ('-' * 60) + '\n' + lista_bandeira[bandeira].upper() + ' SELECIONADO!\n'
                          'Aguarde, processando...\n' + ('-' * 60))

                else:
                    print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))

            except BaseException:
                print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))

            continue

        # SE DINHEIRO, VALIDA DINHEIRO
        elif entrada == 2:
            try:
                lista_opcoes = ["voltar ao menu inicial", "sim", 20, 50, 100]

                notas = int(input('\n--> NÃO HÁ TROCO <--\n'
                                  'INSIRA SOMENTE NOTAS DE: R$' + str(int(lista_opcoes[2])) + ', R$' + str(int(lista_opcoes[3])) + ', R$' + str(int(lista_opcoes[4])) + '\n' +
                                  'DESEJA PROSSEGUIR?\n'
                                  '1 - para ' + lista_opcoes[1] + '\n'
                                  '0 ** para ' + lista_opcoes[0] + '\n'
                                  'DIGITE A OPÇÃO DESEJADA: '))

                if notas == 1 and entrada == 2:
                    print('\n' + ('-' * 60) + '\n' + lista_opcoes[notas].upper() + ' SELECIONADO!\n'
                          'Aguarde, processando...\n' + ('-' * 60))
                    break

                elif notas == 0 and entrada == 2:
                    print('\n' + ('-' * 60) + '\n' + lista_opcoes[notas].upper() + ' SELECIONADO!\n'
                          'Aguarde, processando...\n' + ('-' * 60))
                    continue

                else:
                    print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
                    continue

            except BaseException:
                print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
                continue

        # SE QR Code VALIDA
        elif entrada == 3:
            pass

        # SE OPÇÃO SAIR DO TERMINAL SAIR
        elif entrada == 0:
            print('\nOBRIGADO POR UTILIZAR O POSTO DE COMBUSTÍVEL\n')

        else:
            print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
            continue

    except BaseException:
        print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
        continue

    exit(0)

# BLOCO 2 - INICIA A EXECUÇÃO DO PRÓXIMO ESTADO
if __name__ == '__main__'.startswith:
    runpy.run_module(mod_name=Py_02_Qtd_Tipo_Combustivel)