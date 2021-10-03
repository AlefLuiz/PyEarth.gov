import re
import random
from textwrap import wrap

# Verifica se o campo de e-mail está correto.

def validarEmail(email):
    return re.match(r'[\w-]{1,20}@\w{2,20}\.\w{2,3}$', email)

# Campo de Senha e suas verificações 
# Deve ter pelo menos um número. 
# Deve ter pelo menos uma letra maiúscula e uma minúsculo.
# Deve ter pelo menos um símbolo especial.
# Deve ter entre 6 a 20 caracteres.

def validarSenha(passwd):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pat = re.compile(reg)               
    mat = re.search(pat, passwd)
    if mat:
        return True
    else:
        return False