# Guia para agentes

Este arquivo explica como alterar o Humanizador sem quebrar o pacote nem o prompt.

## O que este repositório contém

O Humanizador é uma skill de agente escrita em Markdown. `SKILL.md` é o prompt que os agentes leem. O repositório não tem etapa de build.

É uma adaptação para o português da skill [Humanizer](https://github.com/blader/humanizer), de blader. Os princípios e a estrutura em seis seções vêm de lá; as listas de palavras, os exemplos e os padrões 10 e 11 foram reescritos para o português. A seção "Texto acadêmico e técnico" e a regra de trocar o adjetivo pelo fato vêm de uma skill de humanização de prosa acadêmica usada em uma tese; mantenha-a geral, sem perfil de voz de uma pessoa específica, porque a amostra de voz do usuário já cobre isso.

Mantenha a skill portátil. Não escreva instruções que a limitem a uma ou duas ferramentas de agente.

## Arquivos principais

- `SKILL.md` é a fonte de verdade e o único arquivo de skill do repositório. Contém metadados YAML portáteis, uma explicação de por que texto de IA soa como soa e padrões numerados agrupados em seis seções e ordenados por força e frequência.
- `README.md` explica instalação, uso e padrões.
- `CHANGELOG.md` guarda as notas de versão, da mais nova para a mais antiga. O histórico da skill original em inglês fica no fim, com os números de padrão que cada versão usava.
- `.claude-plugin/plugin.json` descreve o plugin do Claude e aponta o carregador de skills para o `SKILL.md` da raiz.
- `.claude-plugin/marketplace.json` permite adicionar este repositório como marketplace do Claude.
- `.cursor-plugin/plugin.json` descreve o plugin do Cursor. Omita o caminho `skills` para o Cursor carregar o `SKILL.md` da raiz.
- `agents/openai.yaml` guarda o nome de exibição, a descrição curta e o prompt padrão para agentes compatíveis com a OpenAI.
- `scripts/validate-package.py` confere os arquivos do pacote e os valores compartilhados.
- `scripts/contar-sinais.py` conta em arquivos de texto os sinais que mais sobrevivem a uma reescrita. É uma checagem mecânica para o modo arquivo, não um detector. Se um padrão ganha ou perde uma expressão vigiada forte, atualize a regex correspondente.

## Regras para alterações

Mantenha `SKILL.md` e `README.md` sincronizados.

- **Idioma:** Tudo que o usuário lê fica em português do Brasil: o prompt, o README, as mensagens do validador e os templates de issue. Listas de palavras e exemplos precisam ser em português; não traduza ao pé da letra um sinal do inglês que não existe nesta língua. Mantenha em inglês só identificadores, comandos, nomes de campo e citações da fonte.
- **Padrões:** Os padrões são numerados a partir de 1, sem lacunas, do mais forte e frequente ao mais fraco. Um sinal novo só ganha padrão próprio quando nenhum padrão existente já o implica; prefira dobrá-lo em um padrão existente. Se você adicionar, remover ou renumerar um padrão, atualize as tabelas do README, o título da seção do README e toda referência §. O validador deriva a contagem dos títulos e confere se os nomes dos padrões no README batem com eles.
- **Versão:** Mantenha a mesma versão em `SKILL.md` sob `metadata.version`, no primeiro título `## x.y.z` do `CHANGELOG.md`, em `.claude-plugin/plugin.json` e em `.cursor-plugin/plugin.json`. Não adicione um campo `version` de nível superior à skill.
- **Compatibilidade:** Mantenha as instruções de instalação e uso neutras entre agentes. Nomes como Claude Code, Cursor e Codex são exemplos, não limites.
- **Descrição:** Os manifests do plugin usam a primeira frase da `description` do `SKILL.md`.
- **Tamanho:** Cada palavra do `SKILL.md` é lida a cada uso. O validador limita o arquivo a 8.000 palavras; o português corre cerca de 20% mais longo que o inglês, e a seção de texto acadêmico e técnico ocupa o resto da folga. Uma alteração que acrescenta palavras precisa merecê-las.
- **Histórico:** Adicione uma nota curta ao `CHANGELOG.md` para qualquer mudança de comportamento ou correção não óbvia.
- **Verificações:** Antes de publicar, rode `python3 scripts/validate-package.py`, `npx skills add . --list` e `claude plugin validate .`.

## Estilo de escrita

Use linguagem simples em comentários de código, prompts, documentação, descrições, mensagens de validação e relatórios de progresso.

- Comece pelo ponto principal.
- Use palavras comuns e voz ativa.
- Mantenha frases e parágrafos curtos.
- Use um só termo para o mesmo item.
- Use `deve` para requisitos.
- Use títulos, listas e tabelas quando ajudam o leitor.
- Remova palavras repetidas ou desnecessárias.
- Limite siglas e explique termos técnicos.
- Evite dupla negação.
- Mantenha identificadores, comandos, caminhos, campos de schema, citações, expressões vigiadas e exemplos que carregam comportamento exatamente como estão.
- Mantenha o sentido técnico completo.

## Editando a skill

- Mantenha os metadados YAML válidos.
- Trate o prompt abaixo dos metadados como o produto.
- Prefira uma instrução curta e clara a mais uma exceção ou explicação repetida.
- Aplique a própria skill ao que você escreve aqui. Um README do Humanizador com "vale ressaltar" ou "nesse sentido" é um bug.
