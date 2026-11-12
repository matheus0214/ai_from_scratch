"""Operações com vetores em Python puro.

Um vetor aqui é uma lista de floats. Nenhuma função altera as listas recebidas:
todas devolvem uma lista nova.
"""

Vetor = list[float]

def tamanhos_diferentes(a: int, b: int):
    if a != b:
        raise ValueError("Tamanho dos vetores devem ser iguais")


def somar(a: Vetor, b: Vetor) -> Vetor:
    """Soma dois vetores posição a posição.

    >>> somar([1.0, 2.0], [3.0, 4.0])
    [4.0, 6.0]

    Levanta ValueError se os vetores tiverem tamanhos diferentes.
    """
    tamanhos_diferentes(len(a), len(b))

    soma = []

    for x, v in zip(a, b):
        soma.append(x + v)

    return soma


def subtrair(a: Vetor, b: Vetor) -> Vetor:
    """Subtrai b de a, posição a posição.

    >>> subtrair([5.0, 7.0], [1.0, 2.0])
    [4.0, 5.0]

    Levanta ValueError se os vetores tiverem tamanhos diferentes.
    """
    tamanhos_diferentes(len(a), len(b))

    sub = []

    for x, y in zip(a, b):
        sub.append(x - y)

    return sub


def multiplicar_por_escalar(k: float, v: Vetor) -> Vetor:
    """Multiplica cada posição de v pelo número k.

    >>> multiplicar_por_escalar(3.0, [1.0, 2.0])
    [3.0, 6.0]
    """
    return [k * x for x in v]


def dar_passo(w: Vetor, ajuste: Vetor, taxa: float) -> Vetor:
    """Devolve w - taxa * ajuste: a linha de aprendizado do Capítulo 0, para vários pesos.

    Deve ser escrita usando subtrair e multiplicar_por_escalar, sem laço próprio.

    >>> dar_passo([1.0, 1.0], [10.0, -20.0], 0.1)
    [0.0, 3.0]
    """
    return subtrair(w, multiplicar_por_escalar(taxa, ajuste))
