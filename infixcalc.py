#!/usr/bin/env python
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"
__author__ = "Marcos Teles"
__license__ = "Unlicense"

import sys

arguments = sys.argv[1:]

# TODO: Usar Exception
if not arguments:
    operation = input("Operação: ")
    n1 = input("n1: ")
    n2 = input("n1: ")
    arguments = [operation, n1, n2]

elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments

valid_operation = ("sum", "sub", "mult", "div")

if operation not in valid_operation:
    print("Operação inválida")
    print(valid_operation)
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: Repetição while + Exception
    if not num.replce(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n2, n2 = validated_nums

# TODO: Usar dict de funções
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mult":
    result = n1 * n2
elif operation == "div":
    result = n1 // n2


print(f"Resulto: {result}")
