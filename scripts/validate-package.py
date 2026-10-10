#!/usr/bin/env python3
"""Confere os arquivos do pacote do Humanizador sem dependências externas."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL_NAME = "humanizador"
# Cada palavra do SKILL.md é lida a cada uso. O português corre cerca de 20%
# mais longo que o inglês, e a seção de texto acadêmico e técnico ocupa o
# resto, então o teto é maior que o da skill original.
MAX_SKILL_WORDS = 8000


def read_package_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as error:
        raise SystemExit(f"Não foi possível ler {path.relative_to(ROOT)}: {error}")


SKILL_PATH = ROOT / "SKILL.md"
SKILL = read_package_file(SKILL_PATH)
README = read_package_file(ROOT / "README.md")
CHANGELOG = read_package_file(ROOT / "CHANGELOG.md")
try:
    PLUGIN = json.loads(read_package_file(ROOT / ".claude-plugin" / "plugin.json"))
except json.JSONDecodeError as error:
    raise SystemExit(f"Corrija o JSON em .claude-plugin/plugin.json: {error}")
try:
    CURSOR_PLUGIN = json.loads(
        read_package_file(ROOT / ".cursor-plugin" / "plugin.json")
    )
except json.JSONDecodeError as error:
    raise SystemExit(f"Corrija o JSON em .cursor-plugin/plugin.json: {error}")


def require_match(match: re.Match[str] | None, message: str) -> re.Match[str]:
    if match is None:
        raise SystemExit(message)
    return match


yaml_metadata = require_match(
    re.match(r"\A---\n(.*?)\n---\n", SKILL, re.DOTALL),
    "SKILL.md deve começar com metadados YAML",
).group(1)

for unsupported_field in ("version:", "compatibility:", "allowed-tools:"):
    if re.search(rf"(?m)^{re.escape(unsupported_field)}", yaml_metadata):
        raise SystemExit(f"Remova o campo YAML não suportado: {unsupported_field[:-1]}")

skill_name = require_match(
    re.search(r"(?m)^name:\s*(\S+)\s*$", yaml_metadata),
    "Adicione o campo name aos metadados do SKILL.md",
).group(1)
if skill_name != SKILL_NAME:
    raise SystemExit(f"Defina o nome da skill como {SKILL_NAME}; está {skill_name}")

skill_version = require_match(
    re.search(r'(?m)^\s+version:\s*["\']?([0-9]+\.[0-9]+\.[0-9]+)["\']?\s*$', yaml_metadata),
    "Adicione metadata.version ao SKILL.md como versão de três partes",
).group(1)
changelog_version = require_match(
    re.search(r"(?m)^## ([0-9]+\.[0-9]+\.[0-9]+)$", CHANGELOG),
    "Adicione um título de versão ao CHANGELOG.md",
).group(1)

package_versions = {
    skill_version,
    changelog_version,
    str(PLUGIN.get("version", "")),
    str(CURSOR_PLUGIN.get("version", "")),
}
if len(package_versions) != 1:
    raise SystemExit(
        f"Use uma só versão do pacote em todos os arquivos: {sorted(package_versions)}"
    )

skill_files = {path.relative_to(ROOT) for path in ROOT.rglob("SKILL.md")}
if SKILL_PATH.is_symlink() or skill_files != {Path("SKILL.md")}:
    raise SystemExit("Mantenha um único SKILL.md comum na raiz do repositório")
if PLUGIN.get("name") != SKILL_NAME:
    raise SystemExit(f"Defina o nome do plugin do Claude como {SKILL_NAME}")
if PLUGIN.get("skills") != ["./"]:
    raise SystemExit("Aponte o carregador de skills do plugin do Claude para a raiz do repositório")
if CURSOR_PLUGIN.get("name") != SKILL_NAME:
    raise SystemExit(f"Defina o nome do plugin do Cursor como {SKILL_NAME}")
if "skills" in CURSOR_PLUGIN:
    raise SystemExit("Omita skills do plugin do Cursor para ele carregar o SKILL.md da raiz")

skill_description = " ".join(
    require_match(
        re.search(r"(?m)^description: \|\n((?:  .*\n)+)", yaml_metadata + "\n"),
        "Escreva a description do SKILL.md como bloco indentado",
    ).group(1).split()
)
MARKETPLACE = json.loads(read_package_file(ROOT / ".claude-plugin" / "marketplace.json"))
package_descriptions = {
    str(PLUGIN.get("description", "")),
    str(CURSOR_PLUGIN.get("description", "")),
    *(str(plugin.get("description", "")) for plugin in MARKETPLACE.get("plugins", [])),
}
if len(package_descriptions) != 1 or not skill_description.startswith(
    next(iter(package_descriptions))
):
    raise SystemExit(
        "Use a primeira frase da description do SKILL.md em todos os manifests do plugin: "
        f"{sorted(package_descriptions)}"
    )

skill_patterns = dict(
    (int(number), name)
    for number, name in re.findall(r"(?m)^### ([0-9]+)\. (.+)$", SKILL)
)
pattern_numbers = list(skill_patterns)
pattern_count = len(pattern_numbers)
if pattern_count == 0 or pattern_numbers != list(range(1, pattern_count + 1)):
    raise SystemExit(f"Numere os padrões do SKILL.md a partir de 1 sem lacunas: {pattern_numbers}")

readme_patterns = dict(
    (int(number), name)
    for number, name in re.findall(r"(?m)^\| ([0-9]+) \| \*\*(.+?)\*\*", README)
)
if sorted(readme_patterns) != pattern_numbers:
    raise SystemExit(
        f"Liste os padrões de 1 a {pattern_count} uma vez cada nas tabelas do README: {sorted(readme_patterns)}"
    )
renamed = [
    f"{number}: {readme_patterns[number]!r} deveria ser {name!r}"
    for number, name in skill_patterns.items()
    if readme_patterns[number] != name
]
if renamed:
    raise SystemExit("Iguale os nomes dos padrões do README aos do SKILL.md: " + "; ".join(renamed))
if f"## Os {pattern_count} padrões" not in README:
    raise SystemExit(f"Intitule a seção de padrões do README como 'Os {pattern_count} padrões'")

# Uma renumeração pode deixar uma referência § apontando para o padrão errado
# ou para nada. O CHANGELOG.md guarda os números que cada versão usava, então
# leia só o SKILL.md.
skill_references = sorted({int(number) for number in re.findall(r"§([0-9]+)", SKILL)})
missing_patterns = [
    number for number in skill_references if not 1 <= number <= pattern_count
]
if missing_patterns:
    raise SystemExit(
        f"Aponte toda referência § do SKILL.md para um padrão de 1 a "
        f"{pattern_count}: {missing_patterns}"
    )

skill_words = len(SKILL.split())
if skill_words > MAX_SKILL_WORDS:
    raise SystemExit(
        f"Mantenha o SKILL.md em {MAX_SKILL_WORDS:,} palavras ou menos; ele tem {skill_words:,}".replace(",", ".")
    )

print(f"Pacote do Humanizador v{skill_version} é válido")
