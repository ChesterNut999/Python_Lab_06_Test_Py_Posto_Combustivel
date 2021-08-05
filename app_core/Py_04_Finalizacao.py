# MÓDULO 4 - FINALIZAÇÃO
import sys, time, runpy

# BLOCO 1 - FINAL DE SESSÃO
print('\n' + ('-' * 60) + '\nABASTECIMENTO FINALIZADO!\n' + ('-' * 60) +
      '\nSEU RECIBO ESTÁ SENDO IMPRESSO.\n'
      'Aguarde, processando...', end=' ')

for i in range(0, 6):
    print(i, end=' ')
    sys.stdout.flush()
    time.sleep(1)

print('\n' + ('-' * 60))

# BLOCO 2 - FINAL DE SESSÃO
while True:
    try:
        lista_decisao=['Sair', 'Voltar']

        decisao = (int(input('\nO QUE DESEJA FAZER AGORA?\n'
                             '1 - para ' + lista_decisao[1] + ' ao menu inicial\n'
                             '0 -- para ' + lista_decisao[0] + ' deste terminal\n'
                             'DIGITE A OPÇÃO DESEJADA: ')))

        if decisao == 1:
            print('\n' + ('-' * 60) + '\n' + lista_decisao[decisao].upper() + ' AO MENU INICIAL SELECIONADO!\n'
                  'Aguarde, processando...\n' + ('-' * 60))
            break

        elif decisao == 0:
            break

        else:
            print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
            continue

    except BaseException:
        print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
        continue