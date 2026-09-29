def descobrir_animais(cabecas, pernas):
    coelhos = (pernas - 2 * cabecas) // 2
    galinhas = cabecas - coelhos

    print("Seu Chico tem", galinhas, "galinhas e", coelhos, "coelhos.")


descobrir_animais(35, 94)