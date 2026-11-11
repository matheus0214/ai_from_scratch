# Capítulo 0: Seu Primeiro Modelo

> Volume 0: Primeira Vitória · 1 sessão de 45 minutos · 3 passos

## 🎯 Objetivo do Capítulo

Treinar um modelo de um único parâmetro, do zero, e ver o erro cair no terminal.

**Critério de saída:** o script imprime `OK: seu primeiro modelo aprendeu.`

Este é o único capítulo da coleção em que o código vem guiado linha a linha. O objetivo aqui não é construir peças, é ver a máquina inteira funcionando uma vez. Do Volume 1 em diante, quem escreve é você.

## 🧠 A Intuição (Analogia do Mundo Real)

Pense em acertar a temperatura do chuveiro em um banheiro que você não conhece.

1. Você gira o registro para uma posição qualquer.
2. Põe a mão na água e sente o quanto está longe do que queria.
3. Gira um pouco na direção certa. Se está muito longe, gira mais; se está quase bom, gira pouco.
4. Repete até acertar.

Você nunca calculou a posição correta do registro. Você só mediu o erro e corrigiu um pouco, várias vezes.

Treinar um modelo é exatamente isso:

| Chuveiro | Modelo |
|---|---|
| Posição do registro | O parâmetro `w` |
| Pôr a mão na água | Medir o erro |
| Girar um pouco | Ajustar `w` |
| Repetir | Uma época de treino |

## 📐 A Matemática Sem Mistério

### O problema

Um motorista cobra por quilômetro, mas você não sabe a tarifa. Só tem quatro corridas anotadas:

| Distância `x` (km) | Preço `y` (R$) |
|---|---|
| 1 | 3 |
| 2 | 6 |
| 3 | 9 |
| 4 | 12 |

Você já viu que a tarifa é 3. O modelo não sabe; ele vai descobrir sozinho.

### As três contas

**1. Prever.** O modelo é a aposta mais simples possível: preço = tarifa × distância.

```
chute = w * x
```

**2. Medir o erro.** Com `w = 0` (primeiro chute), na corrida de 2 km:

```
chute     = 0 * 2 = 0
diferenca = chute - y = 0 - 6 = -6
erro      = diferenca² = 36
```

Elevamos ao quadrado por dois motivos: o erro fica sempre positivo, e erros grandes pesam muito mais que erros pequenos. O erro do modelo é a média disso nas quatro corridas.

**3. Ajustar.** Para qual lado girar `w`, e quanto?

```
ajuste = 2 * diferenca * x
w      = w - taxa * ajuste
```

Confira com o exemplo acima: `ajuste = 2 * (-6) * 2 = -24`. Como `w - taxa * (-24)` soma, `w` sobe. Faz sentido: o chute estava baixo demais.

Repare em duas coisas:

- O **sinal** de `diferenca` diz a direção. Chute baixo, `w` sobe; chute alto, `w` desce.
- O **tamanho** de `diferenca` diz a força. Longe do alvo, ajuste grande; perto, ajuste pequeno.

A `taxa` (taxa de aprendizado) é o tamanho da sua mão no registro: quanto você gira a cada tentativa.

> De onde vem o `2 * diferenca * x`? É a derivada do erro em relação a `w`. Por enquanto, aceite como receita. Você vai deduzir isso com as próprias mãos no Volume 1 e usar de verdade no Volume 2.

## 🏗️ Preparando o Projeto

No terminal:

```bash
python3 --version        # precisa ser 3.10 ou maior
cd ~/Projects
mkdir -p ai-from-scratch/{ebooks,libs,tests}
cd ai-from-scratch
git init
touch libs/cap00_primeiro_modelo.py
```

Abra `libs/cap00_primeiro_modelo.py` no editor. **Digite o código, não cole.** São cerca de 20 linhas e digitar é parte do exercício.

## 💻 Os Três Passos

### Passo 1: Prever (10 min)

```python
xs = [1.0, 2.0, 3.0, 4.0]
ys = [3.0, 6.0, 9.0, 12.0]

w = 0.0

for x, y in zip(xs, ys):
    chute = w * x
    print(f"x = {x} | chute = {chute} | real = {y}")
```

Vindo de TypeScript: `zip(xs, ys)` percorre as duas listas em paralelo, como `xs.map((x, i) => [x, ys[i]])`. E `f"..."` é o template literal do Python.

Rode com `python3 libs/cap00_primeiro_modelo.py`.

**Saída esperada:** quatro linhas, todas com `chute = 0.0`. O modelo existe e está completamente errado. Ótimo.

### Passo 2: Medir o erro (10 min)

Substitua o laço do Passo 1 por este:

```python
soma_erro = 0.0
for x, y in zip(xs, ys):
    chute = w * x
    diferenca = chute - y
    soma_erro += diferenca ** 2
erro = soma_erro / len(xs)
print(f"w = {w} | erro = {erro}")
```

**Saída esperada:** `w = 0.0 | erro = 67.5`

Antes de seguir, troque `w = 0.0` por `w = 2.0` e rode de novo. O erro deve cair para `7.5`. Depois teste `w = 3.0`: erro `0.0`. Você acabou de fazer o trabalho do treino na mão. Volte `w` para `0.0`.

### Passo 3: Ajustar e repetir (15 min)

Agora o computador gira o registro por você. O arquivo final fica assim:

```python
xs = [1.0, 2.0, 3.0, 4.0]
ys = [3.0, 6.0, 9.0, 12.0]

w = 0.0
taxa = 0.01

for epoca in range(100):
    soma_erro = 0.0
    soma_ajuste = 0.0
    for x, y in zip(xs, ys):
        chute = w * x
        diferenca = chute - y
        soma_erro += diferenca ** 2
        soma_ajuste += 2 * diferenca * x
    erro = soma_erro / len(xs)
    ajuste = soma_ajuste / len(xs)
    w = w - taxa * ajuste
    if epoca % 10 == 0:
        print(f"epoca {epoca:3d} | w = {w:.4f} | erro = {erro:.4f}")

print(f"w final = {w:.4f}")
assert abs(w - 3.0) < 0.01, "w ainda esta longe de 3; revise o ajuste"
print("OK: seu primeiro modelo aprendeu.")
```

O que mudou em relação ao Passo 2:

- Um laço de fora (`for epoca`) repete tudo 100 vezes.
- `soma_ajuste` acumula o ajuste de cada corrida, e usamos a média.
- A linha `w = w - taxa * ajuste` é o aprendizado. Todo o resto é contabilidade.

## ✅ Como Validar

```bash
python3 libs/cap00_primeiro_modelo.py
```

Saída esperada:

```text
epoca   0 | w = 0.4500 | erro = 67.5000
epoca  10 | w = 2.4980 | erro = 2.6163
epoca  20 | w = 2.9012 | erro = 0.1014
epoca  30 | w = 2.9805 | erro = 0.0039
epoca  40 | w = 2.9962 | erro = 0.0002
epoca  50 | w = 2.9992 | erro = 0.0000
epoca  60 | w = 2.9999 | erro = 0.0000
epoca  70 | w = 3.0000 | erro = 0.0000
epoca  80 | w = 3.0000 | erro = 0.0000
epoca  90 | w = 3.0000 | erro = 0.0000
w final = 3.0000
OK: seu primeiro modelo aprendeu.
```

Ninguém escreveu `3` como resposta em lugar nenhum. O modelo chegou lá medindo o erro e corrigindo.

Se o `assert` falhar, confira nesta ordem: o sinal em `w = w - taxa * ajuste`, a ordem em `chute - y`, e se `soma_ajuste` é zerada dentro do laço de épocas.

Feche com o commit:

```bash
git add . && git commit -m "feat: primeiro modelo treinado do zero"
```

### Se sobrar tempo: dois experimentos (10 min)

Mude só a `taxa`, rode e observe. Depois volte para `0.01`.

1. `taxa = 0.1`: `w` passa do alvo, volta, passa de novo (4.5, 2.25, 3.375...) e ainda assim converge. É você girando o registro com força demais e corrigindo.
2. `taxa = 0.2`: `w` vai para 9, -9, 27, -45... e o erro explode. O `assert` falha. Cada correção é maior que o erro anterior.

Anote esse comportamento. Escolher a taxa de aprendizado é um dos problemas centrais de treinar qualquer modelo, do seu até os grandes.

## 🧩 Checkpoint

Responda sem olhar o código. Se quiser, mande as respostas na próxima sessão.

1. O que acontece com `w` quando o chute está acima do valor real? Por quê?
2. Por que o ajuste fica menor conforme o treino avança, mesmo com a `taxa` fixa?
3. Se os dados fossem `y = 3x + 5`, este modelo conseguiria chegar a erro zero? O que falta nele?

## 🗺️ O Mapa da Coleção

Cada linha do seu script vira um volume:

| No seu script | O que vira | Onde |
|---|---|---|
| `w * x` com um número só | Vetores e matrizes: muitas entradas, muitos pesos | Volume 1 |
| `2 * diferenca * x` | Derivadas: de onde essa receita vem | Volume 1 |
| O laço de épocas | Gradiente descendente e regressão linear completa | Volume 2 |
| Prever um número | Prever sim ou não: perceptron e regressão logística | Volume 3 |
| Um único `w` | Camadas de neurônios e backpropagation | Volume 4 |
| Quatro corridas inventadas | Dataset real, pesos salvos em arquivo | Volume 5 |

O ciclo **prever → medir → ajustar → repetir** não muda mais. Só as peças ficam maiores.

## ➡️ Próximo Passo

Rodar o script até ver o `OK`, fazer o commit e responder as três perguntas do diagnóstico. Com isso, o roadmap da coleção é gerado sob medida.
