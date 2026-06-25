#!/usr/bin/env python3

"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execucao:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Marcos Teles"
__license__ = "Unlicense"

import os

# para mudar a variavel de ambiante responsavel pela lang do sistema
# export LANG=pt_BR.utf8
# snake case
current_language = os.getenv("LANG", "en_US")[:5]

# Complexidade O(1)
msg = {
    "pt_BR": "Olá, mundo!",
    "en_US": "Hello, world!",
    "en_SP": "Hola, Mundo!",
    "it_IT": "Cion, Mondo!",
    "fr_FR": "Bonjuor Monde!"
}

print(msg[current_language])
