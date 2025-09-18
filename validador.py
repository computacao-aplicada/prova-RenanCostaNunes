import re

def validar_cpf(cpf: str) -> bool:
    if not isinstance(cpf, str):
        return False
    cpf_limpo = re.sub(r'[.\-\s]', '', cpf)
    if not cpf_limpo.isdigit() or len(cpf_limpo) != 11:
        return False
    if len(set(cpf_limpo)) == 1:
        return False
    digitos = [int(d) for d in cpf_limpo]
    soma_dv1 = sum(digitos[i] * (10 - i) for i in range(9))
    resto_dv1 = soma_dv1 % 11
    dv1_calculado = 0 if resto_dv1 < 2 else 11 - resto_dv1
    if dv1_calculado != digitos[9]:
        return False
    soma_dv2 = sum(digitos[i] * (11 - i) for i in range(10))
    resto_dv2 = soma_dv2 % 11
    dv2_calculado = 0 if resto_dv2 < 2 else 11 - resto_dv2
    if dv2_calculado != digitos[10]:
        return False
    return True