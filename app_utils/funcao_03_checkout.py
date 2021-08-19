# Este snippet pode ser encontrado em: aqui
# Exemplo de contador para Maurilio Cardoso (part II).

import os
import sys
import time
import re
import termios
import tty

from multiprocessing import Process, Manager
from threading import Timer


def posicao() -> tuple:
    """Essa função pega a posição atual do cursor no terminal.

        Credit: https://stackoverflow.com/a/46675451/16558668

    Returns:
        tuple: Tupla contendo a posição atual do cursor do terminal.
    """

    buffer = ""
    stdin = sys.stdin.fileno()
    tattr = termios.tcgetattr(stdin)

    try:
        tty.setcbreak(stdin, termios.TCSANOW)
        sys.stdout.write("\x1b[6n")
        sys.stdout.flush()

        while True:
            buffer += sys.stdin.read(1)
            if buffer[-1] == "R":
                break

    finally:
        termios.tcsetattr(stdin, termios.TCSANOW, tattr)

    try:
        matches = re.match(r"^\x1b\[(\d*);(\d*)R", buffer)
        groups = matches.groups()

    except AttributeError:
        return None

    return (int(groups[0]), int(groups[1]))


def contagem(num: int, pos: tuple):
    for i in reversed(range(1, num + 1)):
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (pos[0], pos[1], f'====> ESTA SESSÃO SERÁ ENCERRADA EM {str(i).zfill(2)} SEGUNDOS <====\n'))
        sys.stdout.flush()
        time.sleep(1)


def entrada_usuario(fileno: int, retorno: dict, contagem_obj: Process) -> None:
    """Essa função será resposável por capturar a entrada do usuário e armazenará o valor
       no dicionário "retorno".

    Args:
=        fileno (int): File descriptor (nesse caso o stdin).
        retorno (dict): Dicionário "compartilhado". Salvaremos a entrada do usuário aqui.
    """

    sys.stdin = os.fdopen(fileno)

    while True:
        try:
            retorno['entrada'] = int(input('\nVOCE CONFIRMA O CHECKOUT?'
                                           '\n1 - para Sim. Abasteça!'
                                           '\n0 -- para Voltar ao menu inicial'
                                           '\nDIGITE A OPÇÃO DESEJADA: '))

            if retorno['entrada'] == 1 or retorno['entrada'] == 0 or retorno['entrada'] == "":
                contagem_obj.kill()
                break

            else:
                print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
                continue

        except BaseException:
            print('\n' + ('-' * 60) + '\nOPÇÃO INVÁLIDA! ESCOLHA NOVAMENTE.\n' + ('-' * 60))
            continue


def timeout(process: Process):
    """Essa função será responsável por "matar" o processo contendo o input().

    Args:
        process (Process): O processo
    """
    process.kill()


def contador():
    # Dessa vez vamos definir o timeout aqui em cima. (em segundos)
    timeout_value = 10

    # Aqui precisamos pegar o file descriptor 'stdin' para depois passarmos
    # para a função "entrada_usuario". Como ela está em outro processo, não
    # há nenhum fileno associado com o input do teclado. (stdin).
    fileno = sys.stdin.fileno()

    # Utilizaremos um Manager (dict, no caso), para gerenciar alguns objetos entre os processos
    # (uma espécie de proxy).
    manager = Manager()
    retorno = manager.dict()

    # Aqui vamos criar um outro processo responsável por imprimir a mensagem de contagem
    # regressiva na tela. Precisaremos da posição atual do cursor do terminal para podermos
    # imprimir na posição correta (acima do prompt to input).
    pos = posicao()
    process_contagem = Process(target=contagem, args=(timeout_value, pos))

    # Aqui criamos nosso processo que executará a função "entrada_usuario"
    # passando alguns argumentos, como um nome qualquer, o file descriptor (stdin), que é obrigatório
    # para lidarmos com "coisas" vindas do teclado e um dicionário "compartilhado" que utilizaremos
    # para salvar os valores digitados na função. Vamos passar também o "process_contagem" que nada
    # mais é do que o objeto Process da contagem regressiva. Vamos precisar dele para matar o processo
    # de contagem quando o usuário digitar algo "dentro do prazo".
    process_entrada = Process(target=entrada_usuario, args=(fileno, retorno, process_contagem))

    # Aqui criamos um timer. timeout_value contém o valor em segundos do nosso timeout.
    t = Timer(timeout_value, timeout, args=(process_entrada,))
    t.start()

    # Vamos iniciar a contagem também.
    process_contagem.start()

    # Iniciamos nosso processo.
    process_entrada.start()
    process_entrada.join()

    # Após o término do processo (natural ou forçado), cancelamos nosso timer. (afinal, não precisaremos mais dele)
    t.cancel()

# if __name__ == '__main__':
#     contador()