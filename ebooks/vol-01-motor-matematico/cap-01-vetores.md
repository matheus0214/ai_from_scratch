# Capítulo 1: Vetores

> Volume 1: O Motor Matemático · 2 sessões de 45 minutos · 2 missões

## 🎯 Objetivo do Capítulo

Criar o primeiro módulo da sua lib, `minha_math/vetores.py`, com soma, subtração e multiplicação por escalar.

**No fim, roda:** `dar_passo(w, ajuste, taxa)`, a linha de aprendizado do Capítulo 0 funcionando para qualquer quantidade de pesos.

## 🔗 De Onde Viemos

No Capítulo 0 o modelo tinha um único peso, e aprender era uma linha: `w = w - taxa * ajuste`. Um modelo de verdade tem centenas ou milhões de pesos. Para a mesma linha continuar valendo, `w` e `ajuste` precisam deixar de ser números e virar listas de números. Essa lista é o vetor.

## 🧠 A Intuição (Analogia do Mundo Real)

Você já usou vetores toda vez que moveu algo na tela de um jogo.

Um personagem 2D tem uma posição `[x, y]` e uma velocidade `[vx, vy]`. A cada frame:

```
posicao = posicao + velocidade * dt
```

Três ideias estão escondidas aí:

- **Somar vetores** é deslocar: posição mais deslocamento dá a nova posição.
- **Multiplicar por um número** é esticar ou encolher: `velocidade * dt` é a velocidade reduzida ao tamanho de um frame. Se o número for negativo, inverte o sentido.
- **Subtrair vetores** é perguntar "o que falta para ir daqui até ali?": `alvo - posicao` aponta do personagem para o alvo.

Agora compare com o Capítulo 0:

```
posicao = posicao + velocidade * dt
w       = w       - ajuste     * taxa
```

É a mesma conta. Treinar um modelo é mover um ponto, frame a frame, para onde o erro é menor. A única diferença é que o seu personagem vive em 2 dimensões e os pesos de um modelo vivem em quantas dimensões forem necessárias.

Um vetor não precisa ser posição. `[forca, agilidade, vida]` de um personagem também é um vetor, e somar o bônus de um item `[+2, 0, +10]` é a mesma operação.

## 📐 A Matemática Sem Mistério

Tudo neste capítulo é feito **posição a posição**. Não existe mistura entre posições diferentes.

**Soma.** Personagem em `[1, 2]`, deslocamento `[3, 4]`:

```
[1, 2] + [3, 4] = [1 + 3, 2 + 4] = [4, 6]
```

**Subtração.** Personagem em `[1, 2]`, alvo em `[5, 7]`. O que falta?

```
[5, 7] - [1, 2] = [5 - 1, 7 - 2] = [4, 5]
```

A ordem importa: `[1, 2] - [5, 7] = [-4, -5]`, que aponta no sentido contrário.

**Multiplicação por escalar.** "Escalar" é só o nome de um número comum, em oposição a um vetor. Velocidade `[1, 2]` triplicada:

```
3 * [1, 2] = [3 * 1, 3 * 2] = [3, 6]
```

**A regra dos tamanhos.** `[1, 2] + [1, 2, 3]` não tem resposta: a terceira posição não tem par. Não é uma convenção, a conta não existe. A sua lib deve recusar com um erro em vez de devolver algo.

**Faça à mão antes de codar** (confira com os testes depois):

1. `[2, 0, 1] + [1, 1, 1]`
2. `[10, 10] - [3, 12]`
3. `0.5 * [4, -6]`
4. `[1, 1] - 0.1 * [10, -20]`

A conta 4 é o `dar_passo` da Missão 2.

## 🏗️ Arquitetura na Sua Lib

Os arquivos já estão criados na sua pasta:

```text
libs/
└── minha_math/
    ├── __init__.py
    └── vetores.py          <- você implementa aqui
tests/
├── test_v1_c01_m1_soma.py
└── test_v1_c01_m2_escalar.py
```

`vetores.py` tem quatro funções com assinatura e *docstring*, todas com `raise NotImplementedError`:

```python
Vetor = list[float]

def somar(a: Vetor, b: Vetor) -> Vetor: ...
def subtrair(a: Vetor, b: Vetor) -> Vetor: ...
def multiplicar_por_escalar(k: float, v: Vetor) -> Vetor: ...
def dar_passo(w: Vetor, ajuste: Vetor, taxa: float) -> Vetor: ...
```

`Vetor = list[float]` é um apelido de tipo, como `type Vetor = number[]` em TypeScript.

Duas decisões de projeto valem para a lib inteira:

- **Funções puras.** Nenhuma função altera a lista que recebeu; todas devolvem uma lista nova. Os testes verificam isso.
- **Erro explícito.** Tamanhos incompatíveis levantam `ValueError` com uma mensagem que diga os dois tamanhos.

## 💻 Missões

### Missão 1: Somar e subtrair (1 sessão)

**Entrega:** `somar` e `subtrair`.

Passos:

1. Rode o teste antes de escrever qualquer coisa e veja tudo falhar. Esse é o ponto de partida.
2. Em `somar`, comece pela validação: se os tamanhos forem diferentes, levante `ValueError`.
3. Percorra os dois vetores em paralelo (você já fez isso no Capítulo 0) e monte uma lista nova com a soma de cada par.
4. Rode o teste. Quando a classe `TestSomar` passar, faça `subtrair`.
5. Ao terminar `subtrair`, você terá a validação de tamanho escrita duas vezes. Decida o que fazer com isso.

**Critério de saída:** `python3 tests/test_v1_c01_m1_soma.py` termina com `OK` (12 testes).

**Commit:** `feat(minha_math): soma e subtração de vetores`

### Missão 2: Escalar e o passo de aprendizado (1 sessão)

**Entrega:** `multiplicar_por_escalar` e `dar_passo`.

Passos:

1. Implemente `multiplicar_por_escalar`. Aqui não há validação de tamanho: pense por quê.
2. Implemente `dar_passo` **sem escrever nenhum laço**: use apenas as funções que você já tem. Ela deve caber em uma linha.
3. Rode o teste. Um deles reproduz a primeira época do Capítulo 0 (`w = 0.0`, `ajuste = -45.0`, `taxa = 0.01`) e espera `0.45`, o mesmo número que você viu no terminal.

**Critério de saída:** `python3 tests/test_v1_c01_m2_escalar.py` termina com `OK` (11 testes).

**Commit:** `feat(minha_math): multiplicação por escalar e passo de aprendizado`

## ✅ Como Validar

Da raiz do projeto:

```bash
python3 tests/test_v1_c01_m1_soma.py       # Missão 1
python3 tests/test_v1_c01_m2_escalar.py    # Missão 2
```

Para rodar tudo de uma vez: `python3 -m unittest discover -s tests -v`

## 🧩 Checkpoint

Responda sem olhar o código.

1. Por que `multiplicar_por_escalar` não precisa validar tamanhos, e `somar` precisa?
    - O escalar e um número qualquer fixo então e sempre um valor multiplicando por cada elemento do vetor
2. Um personagem está em `[2, 3]` e o alvo em `[10, 3]`. Que conta dá o vetor que aponta do personagem para o alvo, e qual é o resultado?
    - Seria A - P = [10, 3] - [2, 3]
    - Resultado [8, 0]
3. Em `dar_passo`, o que acontece com `w` se a `taxa` for negativa? Relacione com o que você viu no Capítulo 0.
    - Um valor cresce enquanto o outro diminui, vão em direções opostas

## ➡️ Próximo Passo

Missão 1: rodar `python3 tests/test_v1_c01_m1_soma.py`, ver os 12 testes falharem e fazer `somar` passar.
