import time, sys, signal

def timer(contador):
    # for contador in range(30, 0, -1):
    #     time.sleep(1)
    #     sys.stdout.write('\r')
    #
        # if contador > 0:
        #     sys.stdout.write('ESTA SESSÃO SERÁ ENCERRADA EM ' + str(contador) + ' SEGUNDOS')
        #
        # if contador <= 0:
        #     print(('-' * 60) + '\nTEMPO LIMITE ESGOTADO! AGRADECEMOS A COMPREENSÃO.\n' + ('-' * 60))
        #     break

    raise Exception(('-' * 60) + '\nTEMPO LIMITE ESGOTADO! AGRADECEMOS A COMPREENSÃO.\n' + ('-' * 60))

    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(5)

    try:
        signal.alarm(5)
        name = input('Qual é o seu nome? ')
        signal.alarm(0)
        print('Seja bem-vindo,', name)
    except Exception as e:
        print(e)
