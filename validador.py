import re

def _calcular_dv(cpf_parcial: list[int]) -> int:

    soma = sum(
        digito * (len(cpf_parcial) + 1 - i)
        for i, digito in enumerate(cpf_parcial)
    )
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validar_cpf(cpf: str) -> bool:
    if not isinstance(cpf, str):
        return False

    cpf_limpo = re.sub(r'[.\-\s]', '', cpf)
    if not cpf_limpo.isdigit() or len(cpf_limpo) != 11 or len(set(cpf_limpo)) == 1:
        return False

    digitos = [int(d) for d in cpf_limpo]
    dv1_calculado = _calcular_dv(digitos[:9])
    if dv1_calculado != digitos[9]:
        return False
        
    dv2_calculado = _calcular_dv(digitos[:10])
    if dv2_calculado != digitos[10]:
        return False
        
    return True