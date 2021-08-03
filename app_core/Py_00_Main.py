# MÓDULO 0 - MENU DE INICIALIZAÇAO
import runpy, os

import Py_01_FormaPagamento as py1
import Py_02_Qtd_Tipo_Combustivel as py2
import Py_03_Checkout_Abastecimento as py3
import Py_04_Finalizacao as py4

if __name__ == '__main__':
    os.system('clean')

    runpy.run_module(mod_name=py1)

    if py1 is True:
        os.system('clean')
        runpy.run_module(mod_name=py2)

        if py2 is True:
            os.system('clean')
            runpy.run_module(mod_name=py3)

            if py3 is True:
                os.system('clean')
                runpy.run_module(mod_name=py4)

    else:
        exit(0)