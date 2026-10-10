# Humanizador

[![GitHub stars](https://img.shields.io/github/stars/afonsolelis/humanizer?style=flat)](https://github.com/afonsolelis/humanizer/stargazers)

O Humanizador faz texto em português escrito por IA soar como texto escrito por uma pessoa, sem mudar o que ele diz. É uma adaptação para o português da skill [Humanizer](https://github.com/blader/humanizer), de blader, que por sua vez se baseia em [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), o guia que os editores da Wikipédia usam para identificar texto gerado por IA. Funciona no Claude Code, no Codex e em qualquer outro agente que suporte skills.

A versão original traz listas de palavras e exemplos em inglês. A lógica estrutural vale para o português, mas o vocabulário típico de IA nesta língua ("robusto", "alavancar", "nesse sentido", "vale ressaltar", "faz-se necessário") não aparecia nela. Esta versão reescreve as 26 listas e todos os exemplos para o português, adapta dois padrões aos hábitos dos modelos quando escrevem nesta língua e acrescenta uma seção para texto acadêmico e técnico, onde parte do que seria sinal em um post é a voz nativa do gênero.

**Antes:**
> É com grande entusiasmo que anunciamos que os rascunhos compartilhados finalmente chegaram! 🚀 Durante meses, nossa própria equipe se afogava em arquivos chamados final_v7.docx — e sabíamos que precisava haver uma forma melhor. Agora duas pessoas podem editar o mesmo documento ao mesmo tempo, com cada alteração aparecendo ao vivo para ambas. Não é apenas uma funcionalidade; é uma nova forma de colaborar. Vale ressaltar que os comentários permanecem ancorados à frase exata a que se referem, mesmo enquanto o texto ao redor evolui. E o melhor? Está disponível hoje em todos os planos, de forma totalmente gratuita. Pense nisso.

**Depois:**
> Os rascunhos compartilhados saíram hoje. Durante meses a nossa própria equipe passou de mão em mão arquivos chamados final_v7.docx, então criamos um jeito de duas pessoas editarem o mesmo documento ao mesmo tempo, com a alteração de uma aparecendo ao vivo para a outra. Os comentários ficam presos à frase a que se referem, mesmo quando o texto em volta muda. É gratuito em todos os planos.

O Humanizador edita para leitores humanos. Passar por detectores de IA não é um objetivo, e os detectores ainda marcam a maior parte do que ele produz.

## Os cinco sinais mais fortes

Estes são os sinais mais comuns de escrita de IA, e o Humanizador reescreve qualquer um deles à primeira vista:

1. **Não é X, é Y:** "Não é apenas uma funcionalidade, é uma mudança."
2. **Frases de fechamento:** "Pense nisso."
3. **Frases que soam profundas:** "Em sua essência, o que realmente importa é..."
4. **Preparação encenada:** "Vamos mergulhar." "Vale ressaltar que..." "Sinceramente?"
5. **Discutir com ninguém:** "Não estou dizendo que X, mas..."

O Humanizador verifica [26 padrões](#os-26-padrões) ao todo.

## Instalação

Depois de instalada, a skill responde a `/humanizador`.

### Claude Code

```text
/plugin marketplace add afonsolelis/humanizer
/plugin install humanizador@humanizador
```

O plugin responde a `/humanizador:humanizador`. Precisa do Claude Code 2.1.142 ou mais novo; em versões anteriores, use `npx skills add afonsolelis/humanizer --global --agent claude-code`.

### Codex

```bash
npx skills add afonsolelis/humanizer --global --agent codex
```

### Claude.ai e Claude Desktop

Baixe este repositório como ZIP (**Code → Download ZIP**) e envie-o como skill em Configurações.

### Outros agentes

```bash
npx skills add afonsolelis/humanizer --global --agent '*'
```

Isso instala o Humanizador para todo agente que a Skills CLI suporta, incluindo Gemini CLI, GitHub Copilot e Windsurf. Tire o `--global` de qualquer comando acima para instalar só no projeto atual. Para um agente que a Skills CLI não conhece, copie o `SKILL.md` para a pasta de skills dele.

## Uso

Chame a skill diretamente:

```
/humanizador

[cole seu texto aqui]
```

Ou peça em linguagem comum:

```
Humanize este texto: [seu texto]
```

Para reescrever um arquivo, passe o caminho dele:

```
Humanize a prosa em docs/post-de-lancamento.md
```

### Combine com a sua voz

Se quiser que a reescrita soe mais como você, inclua uma amostra:

```
/humanizador

Aqui vai uma amostra da minha escrita para você imitar a voz:
[cole 2 ou 3 parágrafos seus]

Agora humanize este texto:
[cole o texto de IA]
```

O Humanizador segue o ritmo, a escolha de palavras, a pontuação e as manias deliberadas da amostra, inclusive travessões, se você os usa. Ele também mantém a variante do português do texto original, brasileira ou europeia.

## Como funciona

Um modelo de linguagem escreve o que tem mais chance de vir a seguir, então por padrão faz a escolha que serve ao maior número de leitores e assuntos. Uma pessoa escolhe para um leitor e um assunto. Cada sinal que o Humanizador procura é uma forma dessa escolha padrão: uma frase que sinaliza importância em vez de acrescentar um fato, ritmo ou formatação aplicados por regra, um fato comum vestido de decisivo, uma sobra do chat ou uma resposta que reexplica o que o leitor já sabe. Em português, soma-se o registro de redação escolar e de relatório corporativo que os modelos adotam por padrão, com seus conectivos de encadeamento, anúncios de importância e verbos de consultoria.

> "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."
> Wikipédia, ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

O Humanizador marca cada sinal que encontra, do mais forte ao mais fraco. Rascunha uma reescrita sem tratar a estrutura original como fixa, confere o rascunho contra os padrões e contra as afirmações originais, e então escreve a versão final. Ele não inventa nada. Nome, número, data, citação, referência ou qualquer outro detalhe factual precisa vir da fonte ou do autor, e se uma frase precisa de um detalhe que falta, o Humanizador pergunta em vez de inventar.

Em artigo, dissertação, relatório e documentação, o Humanizador calibra o verbo à evidência ("o teste mostrou" para medida direta, "os resultados indicam" para padrão descritivo, "fornece evidência preliminar" para caso único), exige que cada afirmação tenha endereço (seção, quadro, figura ou fonte nomeada), troca o adjetivo de avaliação pelo fato que o gerou e preserva a passagem entre evidência, comparação e mecanismo. A forma impessoal com "se" que tem o artefato como sujeito ("verifica-se no Quadro 3") é tratada como voz legítima do gênero; a que esconde o agente ("faz-se necessário") continua sendo sinal. Em LaTeX, só a prosa muda; comandos, chaves bibliográficas, rótulos, equações e citações literais ficam.

O repositório traz também `scripts/contar-sinais.py`, que conta em um arquivo os sinais que mais sobrevivem a uma reescrita. Serve para comparar o antes e o depois, não para detectar IA.

Quando você cola um texto, o Humanizador mostra o trabalho: a primeira reescrita, uma crítica curta do que ainda soa artificial e a versão final. Aponte-o para um arquivo e ele muda só a prosa, deixando código, dados, metadados e destinos de links em paz. Escrita pessoal mantém as opiniões e as manias do autor. Prosa técnica e de referência fica neutra e simples.

## Os 26 padrões

Os padrões estão numerados por força e frequência. Os cinco primeiros justificam uma edição com uma só ocorrência. Os padrões marcados *fraco sozinho* contam só quando vários sinais dividem o mesmo trecho, porque um autor cuidadoso pode usar qualquer um deles de propósito.

### A. Encenar em vez de afirmar

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 1 | **Não é X, é Y** | "Não é apenas X, é Y", "Isso não significa X. Significa Y.", "Mais do que X, Y" | Diga o ponto diretamente |
| 2 | **Frases de fechamento e fragmentos dramáticos** | "Essa é a verdadeira vitória." depois de toda seção; "...é o que distingue um teste de uma conferência." depois de um fato; "Sem viés. Sem nostalgia." | Corte o fechamento que repete ou explica o exemplo; junte os fragmentos em uma afirmação específica |
| 3 | **Frases que soam profundas** | "Em sua essência, o que realmente importa é...", "Simetria é a linguagem da confiança" | Troque a frase de efeito pela afirmação específica |
| 4 | **Preparação encenada antes do ponto** | "Vamos mergulhar", "Vale ressaltar que...", "Sinceramente? Depende..." | Remova a preparação e diga o ponto |
| 5 | **Discutir com ninguém** | "Não se trata principalmente de...", "Uma abordagem tentadora seria..." | Remova a objeção não levantada ou a opção falsa; mantenha qualquer afirmação real |

### B. Ritmo por regra

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 6 | **Tríades forçadas** | "inovação, inspiração e insights"; três exemplos mais uma lição | Use o número de itens que o sentido pede |
| 7 | **Aberturas de frase repetidas** | "Ela reparou... Ela reparou... Ela guardou..."; três frases do mesmo tamanho e estrutura | Junte as frases, mude o sujeito ou alterne período longo e veredito curto |
| 8 | **Travessão como conector universal** (*fraco sozinho*) | "as instituições — não as pessoas — e ainda assim —" | Use ponto, vírgula, dois-pontos ou parênteses; iguale uma amostra que usa travessões; mantenha o travessão de diálogo |
| 9 | **Qualificadores empilhados** (*fraco sozinho*) | "poderia potencialmente, de certa forma, argumentar-se" | Mantenha só os qualificadores que a fonte sustenta |
| 10 | **Calques do inglês** (*fraco sozinho*) | "endereçar o problema", "entregar valor", "eventualmente o time vai performar" | Use o verbo que um falante usaria: resolver, funcionar, no fim |
| 11 | **Voz passiva, sujeito indeterminado e sujeito oculto** (*fraco sozinho*) | "Faz-se necessário configurar", "Pode-se observar uma melhora" (sem dizer onde) | Nomeie o agente, o lugar ou a medida; "verifica-se no Quadro 3" é voz legítima e fica |

### C. Inflação e autoridade emprestada

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 12 | **Palavras típicas de IA** | "robusto... sólido... consistente... alavancar... nesse sentido... potencializar" | Use palavras simples; troque o adjetivo de avaliação pelo fato que o gerou |
| 13 | **Importância inflada** | "marcando um momento decisivo", "Apesar dos desafios... continua a prosperar", "O futuro é promissor" | Mantenha o fato e tire a importância; termine no último fato concreto |
| 14 | **Conexão ou associação vaga** | "associado à liderança de", "no âmbito de" | Diga a relação que a fonte dá |
| 15 | **Gerúndios de arremate** | "simbolizando... refletindo... evidenciando..." | Mantenha só o que a fonte sustenta |
| 16 | **Linguagem de venda** | "aninhada na deslumbrante região" | Diga o que a coisa é |
| 17 | **Autoridade emprestada** | "Especialistas acreditam...", "a literatura aponta...", "citada na Folha, no Estadão, na BBC e no FT" | Nomeie uma fonte real e o que ela disse, ou remova a afirmação ou a lista |
| 18 | **Evitar é, são e tem** | "serve como... conta com... possui" | "é... tem" |

### D. Formatação por regra

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 19 | **Negrito como decoração** | "**OKRs**, **KPIs**"; "**Desempenho:** O desempenho melhorou" | Remova o negrito; transforme a lista rotulada em prosa |
| 20 | **Títulos decorativos** | "Negociações Estratégicas E Parcerias", "🚀 Fase de Lançamento:", "A decisão, em uma tela" | Maiúscula só na primeira palavra; remova emojis e setas; nomeie o que a seção contém |
| 21 | **Aspas curvas** (*fraco sozinho*) | `disse “o projeto”` em texto digitado | `disse "o projeto"` |

### E. Sobras do chat e do rascunho

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 22 | **Resíduo de chatbot** | "Ótima pergunta! ... Espero que ajude!" | Remova a embalagem e mantenha o conteúdo |
| 23 | **Avisos de limite de conhecimento e chutes** | "Embora os detalhes sejam limitados nas fontes disponíveis, tudo indica que..." | Diga o que a fonte mostra, ou remova a frase |
| 24 | **Título repetido na primeira frase** | "## Desempenho" + "Velocidade importa." | Deixe o título fazer o trabalho |
| 25 | **Escrever sobre o documento em vez de sobre o assunto** | "Esta função foi adicionada para substituir...", "Neste artigo, vamos abordar...", "A tabela abaixo compara..." | Descreva o assunto; declare uma convenção só quando o leitor não a vê |

### F. Escrever para o leitor errado

| # | Padrão | Antes | Depois |
|---|--------|-------|--------|
| 26 | **Reexplicar o que o leitor já sabe** | Uma resposta que percorre o diagnóstico e prova que o plano funciona antes da decisão | Abra com a decisão; deixe o diagnóstico e a prova para o ticket que vem depois |

## Exemplo completo

**Antes (com cara de IA):**
> Recentemente passei cinco dias inesquecíveis em Lisboa, em outubro, e vou te contar — essa cidade roubou completamente o meu coração. Desde o momento em que fiz check-in no meu charmoso hotel, empoleirado no alto do histórico bairro de Alfama, soube que estava em um lugar verdadeiramente especial.
>
> Sim, as famosas ladeiras são desafiadoras — com incontáveis escadas entre o hotel e todo o resto, minhas pernas certamente sentiram! — mas cada subida recompensa com vistas panorâmicas de tirar o fôlego que fazem tudo valer a pena.
>
> Nenhuma viagem estaria completa sem um passeio no icônico Elétrico 28, uma jornada de cerca de quarenta minutos dividida com muitos outros viajantes ansiosos para capturar a magia. E a comida? Simplesmente divina. Embora os pastéis de nata da Pastéis de Belém sejam um amado tesouro nacional, vale ressaltar que o meu favorito veio de uma joia escondida na Graça, ainda quente do forno.
>
> Mas o que realmente torna Lisboa especial não são apenas os pontos turísticos — é a sensação. Caminhe um ou dois quarteirões acima das praças principais e você descobrirá um lado mais tranquilo e autêntico da cidade, que convida a desacelerar e saborear cada momento.
>
> Claro, o imperdível Castelo de São Jorge oferece vistas deslumbrantes sobre os telhados abaixo. As filas podem ser longas, mas a experiência vale absolutamente a pena para qualquer amante de história ou viajante curioso.
>
> Eu voltaria? Com certeza — da próxima vez na primavera, e com sapatos melhores! Lisboa não é apenas um lugar para visitar; é um lugar para se apaixonar, de novo e de novo. ✨

**Depois:**
> Passei cinco dias em Lisboa em outubro. Meu hotel ficava no alto de Alfama, com um monte de escadas entre ele e todo o resto, e minhas pernas sentiram cada uma. As vistas lá de cima compensaram a subida.
>
> Todo mundo diz para andar no Elétrico 28, então andei. O trajeto levou uns quarenta minutos, e a maior parte do bonde era de outros turistas tirando foto pela janela. Os pastéis de nata da Pastéis de Belém são os famosos, mas o meu favorito veio de um lugar na Graça, ainda quente do forno.
>
> A parte de Lisboa de que mais gostei começa um ou dois quarteirões acima das praças principais, onde as ruas ficam quietas e ninguém tem pressa. O Castelo de São Jorge tem uma boa vista sobre os telhados e uma fila longa para chegar até ela.
>
> Eu voltaria, na primavera da próxima vez, e com sapatos melhores.

## Fontes

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) é a fonte da lista de padrões.
- [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) mantém a página.
- [blader/humanizer](https://github.com/blader/humanizer) é a skill original em inglês da qual esta versão deriva.

## Histórico de versões

Veja [CHANGELOG.md](CHANGELOG.md).

## Licença

MIT

Se o Humanizador te ajudou, uma estrela ajuda outras pessoas a encontrá-lo.
