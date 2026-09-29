def buscar_permissao(perfis, perfil, indice):
    try:
        return perfis[perfil][indice]

    except KeyError:
        return "acesso_restrito"

    except IndexError:
        return "acesso_restrito"