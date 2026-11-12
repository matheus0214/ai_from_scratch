"""Volume 1, Capítulo 1, Missão 1: somar e subtrair vetores.

Rode da raiz do projeto:  python3 tests/test_v1_c01_m1_soma.py
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "libs"))

from minha_math.vetores import somar, subtrair


class TestSomar(unittest.TestCase):
    def test_soma_posicao_a_posicao(self):
        self.assertEqual(somar([1.0, 2.0], [3.0, 4.0]), [4.0, 6.0])

    def test_funciona_com_qualquer_tamanho(self):
        self.assertEqual(somar([1.0, 2.0, 3.0, 4.0], [10.0, 20.0, 30.0, 40.0]), [11.0, 22.0, 33.0, 44.0])

    def test_negativos(self):
        self.assertEqual(somar([1.0, -2.0], [-1.0, 2.0]), [0.0, 0.0])

    def test_vetores_vazios(self):
        self.assertEqual(somar([], []), [])

    def test_tamanhos_diferentes_levanta_erro(self):
        with self.assertRaises(ValueError):
            somar([1.0, 2.0], [1.0, 2.0, 3.0])

    def test_nao_altera_as_entradas(self):
        a, b = [1.0, 2.0], [3.0, 4.0]
        somar(a, b)
        self.assertEqual(a, [1.0, 2.0])
        self.assertEqual(b, [3.0, 4.0])

    def test_devolve_lista_nova(self):
        a = [1.0, 2.0]
        self.assertIsNot(somar(a, [0.0, 0.0]), a)


class TestSubtrair(unittest.TestCase):
    def test_subtrai_posicao_a_posicao(self):
        self.assertEqual(subtrair([5.0, 7.0], [1.0, 2.0]), [4.0, 5.0])

    def test_a_ordem_importa(self):
        self.assertEqual(subtrair([1.0, 2.0], [5.0, 7.0]), [-4.0, -5.0])

    def test_vetor_menos_ele_mesmo_da_zero(self):
        v = [3.0, -1.5, 8.0]
        self.assertEqual(subtrair(v, v), [0.0, 0.0, 0.0])

    def test_tamanhos_diferentes_levanta_erro(self):
        with self.assertRaises(ValueError):
            subtrair([1.0], [1.0, 2.0])

    def test_nao_altera_as_entradas(self):
        a, b = [5.0, 7.0], [1.0, 2.0]
        subtrair(a, b)
        self.assertEqual(a, [5.0, 7.0])
        self.assertEqual(b, [1.0, 2.0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
