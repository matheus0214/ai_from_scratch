# Roadmap da Coleção: IA do Zero em Python Puro

Gerado em 11/11/2026 a partir do diagnóstico.

## Como este roadmap foi adaptado a você

| Diagnóstico | O que mudou no plano |
|---|---|
| Escreve Python com fluência | Não há capítulo de Python. As missões vão direto para a matemática e cobram *type hints* e testes desde a primeira. |
| Não lembra de derivada nem de multiplicação de matrizes | O Volume 1 é mais longo e mais lento: toda conta é feita à mão com números pequenos antes de virar código, e derivada e multiplicação de matrizes ganham capítulos próprios. |
| Quer mudar de área | Todo volume termina com algo publicável no GitHub. A trilha final (autograd, modelo de linguagem, ponte para `numpy` e `pytorch`) deixa de ser opcional: construir do zero prova que você entende, mas as vagas pedem as ferramentas reais. |

## Visão geral

| Volume | Lib | Sessões (45 min) | No fim, roda |
|---|---|---|---|
| 0. Primeira Vitória | (script único) | 1 | Um modelo que descobre a tarifa sozinho |
| 1. O Motor Matemático | `minha_math` | ~14 | Gradiente numérico de qualquer função |
| 2. O Primeiro Modelo Preditivo | `minha_regressao` | ~11 | Previsão de preços a partir de um CSV |
| 3. Classificação Binária | `meu_classificador` | ~10 | Um classificador com métricas |
| 4. Redes Neurais | `minha_mlp` | ~17 | Uma rede que aprende XOR |
| 5. Projeto Final | (todas juntas) | ~11 | Treino em dataset real, com pesos salvos e CLI |
| 6. Ponte para o Mercado | `meu_autograd` | ~12 | A mesma rede em `numpy` e `pytorch` |

Total aproximado: **76 sessões**. A estimativa é grosseira e será corrigida no `PROGRESSO.md` conforme o ritmo real.

Regra de avanço: um volume só começa quando o critério de conclusão do anterior roda.

---

## Volume 0: Primeira Vitória

- **Objetivo do projeto:** ver o ciclo prever → medir → ajustar → repetir funcionando antes de construir as peças.
- **Lib:** nenhuma; um script em `libs/cap00_primeiro_modelo.py`.
- **Funcionalidades entregues:** modelo `y = w * x` treinado em quatro pontos.
- **Sessões:** 1.
- **Critério de conclusão:** o script imprime `OK: seu primeiro modelo aprendeu.`

Capítulos: 0. Seu Primeiro Modelo.

## Volume 1: O Motor Matemático

- **Objetivo do projeto:** construir a caixa de ferramentas que todos os modelos seguintes usam, reaprendendo a matemática do zero.
- **Lib:** `minha_math`.
- **Funcionalidades entregues:** operações com vetores, produto escalar, norma, matrizes (forma, transposta, multiplicação), derivada numérica e gradiente numérico.
- **Sessões:** ~14.
- **Critério de conclusão:** `gradiente_numerico(f, ponto)` devolve o gradiente correto de uma função de várias variáveis, e todos os testes de `tests/` passam.

Capítulos:

1. Vetores: soma, subtração e multiplicação por escalar (2 missões)
2. Produto escalar e norma: medir semelhança e tamanho (2 missões)
3. Matrizes: forma, acesso e transposta (2 missões)
4. Multiplicação de matrizes, devagar: matriz × vetor, depois matriz × matriz (3 missões)
5. Inclinação e derivada: o quanto a saída muda quando a entrada muda (3 missões)
6. Derivadas parciais e gradiente: a derivada com várias entradas (2 missões)

## Volume 2: O Primeiro Modelo Preditivo

- **Objetivo do projeto:** refazer o Capítulo 0 como uma biblioteca de verdade, com várias entradas.
- **Lib:** `minha_regressao`.
- **Funcionalidades entregues:** erro quadrático médio, gradiente descendente, regressão linear múltipla, normalização, divisão treino e teste.
- **Sessões:** ~11.
- **Critério de conclusão:** o modelo treina em um CSV de preços e o erro no conjunto de teste fica abaixo de uma linha de base (prever sempre a média).

Capítulos:

1. Função de custo: o erro quadrático médio (2 missões)
2. Gradiente descendente em uma variável (2 missões) · visualização interativa
3. Regressão linear com várias entradas (3 missões)
4. Normalização e divisão treino e teste (2 missões)
5. Mini-projeto: prever preços a partir de um CSV (2 missões)

## Volume 3: Classificação Binária

- **Objetivo do projeto:** sair de "prever um número" para "decidir sim ou não".
- **Lib:** `meu_classificador`.
- **Funcionalidades entregues:** perceptron, sigmoide, *log loss*, regressão logística, acurácia, precisão e *recall*.
- **Sessões:** ~10.
- **Critério de conclusão:** o classificador separa um conjunto de dados de duas classes e imprime as três métricas no conjunto de teste.

Capítulos:

1. Perceptron: uma linha que separa dois grupos (3 missões) · visualização interativa
2. Sigmoide: de pontuação para probabilidade (2 missões)
3. *Log loss* e regressão logística (3 missões)
4. Métricas: acurácia, precisão e *recall* (2 missões)

## Volume 4: Redes Neurais

- **Objetivo do projeto:** empilhar neurônios e fazer o erro voltar pela rede.
- **Lib:** `minha_mlp`.
- **Funcionalidades entregues:** neurônio, camada, funções de ativação, *forward pass*, backpropagation, verificação de gradiente.
- **Sessões:** ~17.
- **Critério de conclusão:** a rede aprende XOR, e o gradiente do backpropagation bate com o gradiente numérico do Volume 1.

Capítulos:

1. Neurônio e camada (2 missões)
2. Funções de ativação e suas derivadas (2 missões) · visualização interativa
3. *Forward pass*: da entrada à saída (2 missões)
4. Regra da cadeia, à mão (3 missões)
5. Backpropagation (4 missões) · visualização interativa
6. Verificação de gradiente: provar que o backpropagation está certo (2 missões)
7. Treinar XOR (2 missões)

## Volume 5: Projeto Final Integrado

- **Objetivo do projeto:** usar as suas libs em um problema real, do CSV à predição.
- **Lib:** todas as anteriores, integradas.
- **Funcionalidades entregues:** leitura de dataset em CSV, treino e avaliação, pesos salvos e carregados em JSON, comando de predição no terminal, README de apresentação.
- **Sessões:** ~11.
- **Critério de conclusão:** `python3 -m prever <entradas>` carrega os pesos salvos e devolve a classe, e o repositório está público com README.

Capítulos:

1. Carregar e preparar um dataset real (Iris) (2 missões)
2. Treinar e avaliar a rede (3 missões)
3. Salvar e carregar pesos em JSON (2 missões)
4. Comando de predição no terminal (2 missões)
5. README e publicação no GitHub (2 missões)

## Volume 6: Ponte para o Mercado

- **Objetivo do projeto:** ligar o que você construiu às ferramentas que o mercado usa.
- **Lib:** `meu_autograd`.
- **Funcionalidades entregues:** motor de autograd escalar, modelo de linguagem bigrama por caracteres, a MLP do Volume 4 reescrita em `numpy` e em `pytorch`.
- **Sessões:** ~12.
- **Critério de conclusão:** as três versões da rede (a sua, `numpy`, `pytorch`) chegam ao mesmo resultado no dataset do Volume 5, com uma tabela no README comparando cada função sua com a equivalente.

Capítulos:

1. Autograd escalar: derivadas calculadas automaticamente (4 missões)
2. Modelo de linguagem bigrama por caracteres (4 missões)
3. A mesma rede em `numpy` e `pytorch` (4 missões)

Este é o único volume em que bibliotecas externas entram, e só no capítulo 3.

---

## Onde você está

Volume 0, Capítulo 0. Próximo passo: rodar o script até imprimir o `OK`.
