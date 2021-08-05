# MÓDULO 0 - MENU DE INICIALIZAÇAO
import runpy, os
import Py_01_FormaPagamento
import Py_02_Qtd_Tipo_Combustivel
import Py_03_Checkout_Abastecimento
import Py_04_Finalizacao

# BLOCO 1 - EXECUÇAO DOS MODULOS
if __name__ == '__main__':
    runpy.run_module(mod_name=Py_01_FormaPagamento.entrada)

    if Py_02_Qtd_Tipo_Combustivel is True:
        os.system('clear' or None)
        runpy.run_module(mod_name=Py_03_Checkout_Abastecimento)

        if Py_03_Checkout_Abastecimento is True:
            os.system('clear' or None)
            runpy.run_module(mod_name=Py_04_Finalizacao)

            if Py_04_Finalizacao is True:
                os.system('clear' or None)

            elif Py_04_Finalizacao.decisao == 0:
                exit(0)

        elif Py_03_Checkout_Abastecimento.checkout == 0:
            exit(0)

    else:
        exit(0)