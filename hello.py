#!/usr/bin/env python3

"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Informe atraves do CLI argument '--lang'

Ou o usuario tera que digitar

Execucao:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Marcos Teles"
__license__ = "Unlicense"

import os
import sys


arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

# para mudar a variavel de ambiante responsavel pela lang do sistema
# export LANG=pt_BR.utf8
# snake case
current_language = arguments["lang"]

if current_language is None:
    current_language = os.getenv("LANG")
    # TODO: Usar repeticoes
    if current_language is None:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

# Complexidade O(1)
msg = {
    "pt_BR": "Olá, mundo!",
    "en_US": "Hello, world!",
    "en_SP": "Hola, Mundo!",
    "it_IT": "Cion, Mondo!",
    "fr_FR": "Bonjuor Monde!"
}

print(msg[current_language] * int(arguments["count"]))
