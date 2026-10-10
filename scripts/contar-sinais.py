#!/usr/bin/env python3
"""Conta, em arquivos de texto em português, os sinais de IA que mais sobrevivem a uma reescrita.

Uso: python3 scripts/contar-sinais.py ARQUIVO [ARQUIVO...]

Cada linha da saída traz OK ou VER, o caminho e a contagem por sinal. A contagem é
uma checagem mecânica para antes e depois de uma reescrita, não um detector de IA:
um texto humano pode ter qualquer um destes sinais de propósito.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SINAIS = [
    ("travessao", r"—"),
    ("meia-risca", r"–"),
    ("hifen-travessao", r"(?<=\w) - (?=\w)"),
    ("nao-X-mas-Y", r"\bn[ãa]o (é |se trata )?(apenas|s[óo]|somente|meramente)\b[^.\n]{0,90}\b(mas|é)\b"),
    ("aforismo", r"\b(é o que (distingue|diferencia|separa|sustenta|garante|importa)|é o cuidado que|é a verdadeira|pense nisso|simples assim)\b"),
    ("anuncio", r"\b(vale (ressaltar|destacar|lembrar|mencionar|notar)|é importante (ressaltar|destacar|notar)|cabe (destacar|ressaltar|salientar)|cumpre observar|nesse sentido|vamos mergulhar)\b"),
    ("lexico", r"\b(robust|s[óo]lid|consistent|coerent|crucial|fundamental|essencial|alavanc|potencializ|impulsion|aprimor|fomenta|viabiliz|abrangent|hol[íi]stic|sinergi|paradigm|disruptiv|multifacetad|imprescind[íi]ve)\w*"),
    ("gerundio-arremate", r",\s+(destacando|ressaltando|enfatizando|evidenciando|demonstrando|refletindo|simbolizando|reforçando|garantindo|contribuindo|promovendo|consolidando)\b"),
    ("se-enchimento", r"\b(faz-se necess[áa]ri|torna-se (imprescind[íi]vel|necess[áa]ri|fundamental)|é poss[íi]vel (observar|notar|verificar|perceber))\w*"),
    ("calque", r"\b(endere[çc]ar|performa[rn]|entregar valor|agregar valor|ao final do dia|startar|deletar|customizar|printar)\w*"),
    ("negrito-rotulo", r"^\s*[-*]\s+\*\*[^*\n]+:\*\*"),
    ("emoji-seta", r"[\U0001F300-\U0001FAFF✅→]"),
    ("aspas-curvas", r"[“”]"),
    ("chatbot", r"\b(espero que (ajude|tenha ajudado)|[óo]tima pergunta|com certeza!|claro!|fique [àa] vontade|me avise se)\b"),
]


def contar(texto: str) -> list[tuple[str, int]]:
    achados = []
    for nome, padrao in SINAIS:
        n = len(re.findall(padrao, texto, re.IGNORECASE | re.MULTILINE))
        if n:
            achados.append((nome, n))
    return achados


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    codigo = 0
    for caminho in argv[1:]:
        p = Path(caminho)
        try:
            texto = p.read_text(encoding="utf-8")
        except OSError as erro:
            print(f"ERRO {caminho}: {erro}", file=sys.stderr)
            codigo = 1
            continue
        achados = contar(texto)
        if achados:
            codigo = max(codigo, 1)
            detalhe = "  " + " ".join(f"{nome}={n}" for nome, n in achados)
            print(f"VER  {caminho}{detalhe}")
        else:
            print(f"OK   {caminho}")
    return codigo


if __name__ == "__main__":
    sys.exit(main(sys.argv))
