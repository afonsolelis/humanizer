# Changelog

## 1.1.0

Traz para o Humanizador a visão de uma skill de humanização de prosa acadêmica usada em uma tese de doutorado em português.

- Nova seção "Texto acadêmico e técnico" depois de Voz: calibrar o verbo à evidência (mostrou, indica, fornece evidência preliminar, uma interpretação possível é), dar endereço a cada afirmação (seção, quadro, figura, fonte nomeada), trocar o adjetivo de avaliação pelo fato que o gerou, separar observação de interpretação e de conclusão, preservar a passagem entre evidência, comparação e mecanismo, manter a retomada de conceitos que sustenta o argumento e nunca reescrever citações literais.
- O padrão 11 distingue a forma com "se" que tem o artefato como sujeito e um endereço ("verifica-se no Quadro 3"), que é voz legítima do gênero, da que esconde o agente ou enche a frase ("faz-se necessário", "pode-se observar uma melhora"). Ganhou um exemplo de forma legítima a deixar em paz.
- O padrão 2 inclui os aforismos de fechamento do registro formal e de avaliação ("é o que distingue", "é o que sustenta", "é o cuidado que"), com exemplo próprio, e a regra de que a generalização, quando é o ponto, vira a frase principal.
- O padrão 4 inclui "chama atenção que", "um trecho merece destaque porque", "o que salta aos olhos" e "aqui vale uma observação".
- O padrão 7 cobre também sequências de frases do mesmo tamanho e estrutura, e pede a alternância entre período longo e veredito curto.
- O padrão 12 inclui sólido, consistente, coerente, alinhado, maduro, bem estruturado, notório, exemplar, nítido e consolidado; manda trocar o adjetivo pelo fato e não por sinônimo; e poupa os conectivos que explicam uma relação (já que, porém, visto que, ou seja, mesmo que, devido a).
- O padrão 17 inclui "a literatura aponta", "autores defendem" e "diversos autores".
- O modo arquivo preserva comandos LaTeX, chaves bibliográficas, rótulos, referências cruzadas, equações e a vírgula decimal.
- "Quando não agir" proíbe atribuir autoria humana ou artificial por estilo ou data, e guarda como voz o veredito seco, a concessão na mesma frase do elogio e a dúvida honesta.
- Novo `scripts/contar-sinais.py`, que conta em arquivos os sinais que mais sobrevivem a uma reescrita, para comparar antes e depois no modo arquivo.
- O teto do SKILL.md sobe para 8.000 palavras.

## 1.0.0

Primeira versão em português, derivada da versão 3.1.0 da skill [Humanizer](https://github.com/blader/humanizer), de blader.

- A skill passa a se chamar `humanizador` e responde a `/humanizador`, para não colidir com a original em inglês quando as duas estão instaladas.
- O prompt, o README, o guia para agentes, os templates de issue e as mensagens do validador foram reescritos em português do Brasil.
- As listas de "fique atento a" dos 26 padrões foram reescritas com o vocabulário que os modelos usam em português: "robusto", "alavancar", "potencializar", "nesse sentido", "vale ressaltar", "faz-se necessário", "possui", "desempenha um papel fundamental", entre outros.
- Os anúncios de importância do registro formal ("vale ressaltar que", "é importante destacar que", "cabe salientar que") entraram no padrão 4, com exemplo próprio.
- O padrão 10, que em inglês tratava de pares hifenizados, virou "Calques do inglês": "endereçar um problema", "performar", "entregar valor", "eventualmente" no sentido de "por fim".
- O padrão 11 ganhou as formas de sujeito indeterminado do registro acadêmico e burocrático: "faz-se necessário", "pode-se observar", "verifica-se que".
- O padrão 8 mantém o travessão que abre fala de personagem, que é a norma do português em ficção, e aplica a regra só ao travessão que une orações.
- O padrão 21 explica que a aspa curva é a norma do português editado, e que o sinal é a aspa curva em texto digitado, Markdown ou código.
- A seção Voz pede que a reescrita mantenha a variante do original, brasileira ou europeia, e o registro dominante entre "você" e "tu".
- "Quando não agir" avisa que o registro formal de redação e relatório já usava esses termos antes dos modelos, então o sinal é a densidade ou o gênero errado.
- Todos os exemplos foram traduzidos ou substituídos por exemplos em português. O exemplo completo do README e o do anúncio de rascunhos compartilhados foram reescritos.
- O validador confere o título `## Os 26 padrões` no README, o nome `humanizador` no plugin do Cursor e um teto de 7.000 palavras no `SKILL.md`.
- O resultado do teste cego da versão original (16 de 16) não foi repetido com a versão em português e, por isso, saiu do README.

## Histórico da skill original (em inglês)

As notas abaixo são da skill de blader e mantêm os números de padrão que cada versão usava. A versão 1.0.0 acima parte da 3.1.0.

### 3.1.0

- Added pattern #26 and section F for replies that re-explain context the reader already has (#269). It acts on replies, not standalone writing. 26 patterns total.
- Extended the core rule so "something the reader did not already have" counts the surrounding conversation, not only earlier text.
- Widened #25 to text that describes its own sourcing, assembly, or layout (#290), and added headings written for effect to #20.
- Extended #2 to "That distinction matters." (#277) and to a sentence that explains what an example already showed (#295).
- Narrowed #10 so words the dictionary always hyphenates keep their hyphen. Gave each watched word one pattern, and stated the evidence rule and the no-invention rule once each.
- Fixed the Voice section's dash reference (#273) and the marketplace schema URL (#288).
- Added a Cursor plugin manifest (#278).
- README: opens with a before/after, the five strongest tells, and install steps for each agent. States that getting past AI detectors is not a goal. The full example's rewrite now keeps every fact from its draft and adds none. Version history moved to this file.

### 3.0.0

Rebuilt the skill around one account of why AI text sounds the way it does, and consolidated 35 patterns into 25. Patterns are grouped in five sections and numbered by strength and frequency, so the not-X-but-Y contrast and the one-line closer come first and get the fullest treatment. Merged duplicate guidance: the workflow is one section instead of five, the dash rule is stated once, and each false-positive guard lives inside its pattern. Realigned with the current Wikipedia article: dropped false ranges and synonym cycling, which Wikipedia now lists as human habits or historical, added vague connection or association, and extended the watch lists for words, notability, copulatives, sales language, disclaimers, and Markdown formatting. Reordered the README and removed the `ai-detection` keyword from the package files. Old to new numbers: 1→13, 2→17, 3→15, 4→16, 5→17, 6→13, 7→12, 8→18, 9→1, 10→6, 11→7, 12→dropped, 13→11, 14→8, 15→19, 16→19, 17→20, 18→20, 19→21, 20→22, 21→23, 22→22, 23→dropped, 24→9, 25→13, 26→10, 27→3, 28→4, 29→24, 30→25, 31→2, 32→3, 33→4, 34→5, 35→5.

### 2.11.3

Grouped patterns 26-35 under "More style patterns" in the skill and README (fixes #247). Kept inline code, commands, paths, and URLs out of the dash rule and file mode edits. Step 3 now keeps every supported claim, allows a removal that a pattern requires, and checks that rankings and simultaneity claims survive shape edits (fixes #212). Explained in §9 why the not-X-but-Y form appears and when to keep it. Added decorative arrows to §18 and pause commands and one-word shouting to §31. The text given to the skill is content to edit, never instructions (#238). No change to the 35 patterns.

### 2.11.2

Removed the plugin symlink and separate Claude Desktop package. Current Claude Code loads the root `SKILL.md` directly, so GitHub's source ZIP now works in Claude Desktop. No change to the 35 patterns.

### 2.11.1

Added a Claude Desktop-ready release package with one regular `humanizer/SKILL.md` file. GitHub's source archive still keeps the plugin symlink (fixes #224). No change to the 35 patterns.

### 2.11.0

Rewrote all repo guidance, descriptions, checks, and skill instructions in Plain Language. Kept all 35 patterns and their behavior.

### 2.10.2

Added the standard `skills/humanizer/` plugin path for Claude Desktop and older loaders. The path links to the root skill, so there is still one prompt (fixes #202).

### 2.10.1

Added figurative uses of `gate`, `gated`, and `gating` to §7. Kept real technical uses, such as feature gating and CI quality gates.

### 2.10.0

Added patterns #34 and #35 for old drafting ideas left in final text. Added safeguards for real limits, objections, and alternatives (fixes #198). Also improved §24 and the final rewrite step. 35 patterns total.

### 2.9.2

Added repeated sentence openings to pattern #11, with a safeguard for deliberate repetition (fixes #206). Expanded §28 to cover casual announcements. 33 patterns total.

### 2.9.1

Improved installation and package checks. Removed unsupported metadata, tool approvals, and a repeated long example. 33 patterns total.

### 2.9.0

Added the rule against invented facts and updated every example to follow it (fixes #187). Made information more important than paragraph shape, let writing samples override §14, and added three output modes. 33 patterns total.

### 2.8.3

Moved the version to `metadata.version` for Agent Skills compatibility. 33 patterns total.

### 2.8.2

Replaced the main example with a first-person Lisbon story that keeps the original topic, view, and detail. 33 patterns total.

### 2.8.1

Added cross-agent installation, Claude plugin files, and a safeguard for quoted text. 33 patterns total.

### 2.8.0

Added patterns #31-33 and expanded pattern #20 to catch chatbot offers. 33 patterns total.

### 2.7.0

Added pattern #30, strengthened the dash rule, and expanded pattern #21 to cover unsupported guesses. 30 patterns total.

### 2.6.0

Combined repeated workflow text, limited personality guidance to the right content, removed model guesses, and shortened the main example. 29 patterns total.

### 2.5.1

Added passive voice and missing subjects. 29 patterns total.

### 2.5.0

Added deeper-truth claims, announcements, repeated headings, and clipped negative endings. Tightened the dash rule and corrected the frontmatter. 28 patterns total.

### 2.4.0

Added writing-sample matching.

### 2.3.0

Added hyphenated word pairs.

### 2.2.0

Added a draft check and second rewrite.

### 2.1.1

Corrected the curly-quote example.

### 2.1.0

Added before/after examples for all 24 patterns.

### 2.0.0

Rewrote the skill from the Wikipedia source.

### 1.0.0

First release.
