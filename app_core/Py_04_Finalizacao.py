# MÓDULO 4 - FINALIZAÇÃO
import sys, time, runpy

import Py_01_FormaPagamento, Py_02_Qtd_Tipo_Combustivel, Py_03_Checkout_Abastecimento

# BLOCO 1 - FINAL DE SESSÃO
print('\n' + ('-' * 60) + '\nABASTECIMENTO FINALIZADO!\n' + ('-' * 60) +
              '\nSEU RECIBO ESTÁ SENDO IMPRESSO.\n'
              'Aguarde, processando...', end=' ')

for i in range(0, 6):
    print(i, end=' ')
    sys.stdout.flush()
    time.sleep(1)

print('\n' + ('-' * 60))

while True:
    try:
        lista_decisao=['sair', 'voltar ao menu inicial']

        decisao = (int(input('\nFINALIZE SUA SESSÃO. AGRADECEMOS A PREFERÊNCIA!\n'
                     # '1 - para ' + lista_decisao[1] + '\n'
                     '0 ** para ' + lista_decisao[0] + ' deste terminal\n'
                     'DIGITE A OPÇÃO DESEJADA: ')))

        # if decisao == 1:
        #     if __name__ == '__main__':
        #         runpy.run_module(mod_name=py_01)

        if decisao == 0:
            print('\nOBRIGADO POR UTILIZAR O POSTO DE COMBUSTÍVEL\n')
            break

        else:
            print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))

    except BaseException:
        print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
        continue


