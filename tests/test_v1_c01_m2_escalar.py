"""Volume 1, Capítulo 1, Missão 2: multiplicar por escalar e dar um passo.

Rode da raiz do projeto:  python3 tests/test_v1_c01_m2_escalar.py
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "libs"))

from minha_math.vetores import dar_passo, multiplicar_por_escalar


class TestMultiplicarPorEscalar(unittest.TestCase):
    def test_multiplica_cada_posicao(self):
        self.assertEqual(multiplicar_por_escalar(3.0, [1.0, 2.0]), [3.0, 6.0])

    def test_escalar_zero_zera_o_vetor(self):
        self.assertEqual(multiplicar_por_escalar(0.0, [5.0, -7.0, 2.0]), [0.0, 0.0, 0.0])

    def test_escalar_negativo_inverte_o_sentido(self):
        self.assertEqual(multiplicar_por_escalar(-1.0, [2.0, -3.0]), [-2.0, 3.0])

    def test_escalar_fracionario_encolhe(self):
        self.assertEqual(multiplicar_por_escalar(0.5, [4.0, 10.0]), [2.0, 5.0])

    def test_vetor_vazio(self):
        self.assertEqual(multiplicar_por_escalar(9.0, []), [])

    def test_nao_altera_a_entrada(self):
        v = [1.0, 2.0]
        multiplicar_por_escalar(3.0, v)
        self.assertEqual(v, [1.0, 2.0])


class TestDarPasso(unittest.TestCase):
    def test_passo_com_dois_pesos(self):
        self.assertEqual(dar_passo([1.0, 1.0], [10.0, -20.0], 0.1), [0.0, 3.0])

    def test_reproduz_a_primeira_epoca_do_capitulo_0(self):
        # No Capítulo 0: w = 0.0, ajuste = -45.0, taxa = 0.01  ->  w = 0.45
        resultado = dar_passo([0.0], [-45.0], 0.01)
        self.assertEqual(len(resultado), 1)
        self.assertAlmostEqual(resultado[0], 0.45)

    def test_taxa_zero_nao_sai_do_lugar(self):
        self.assertEqual(dar_passo([2.0, 3.0], [100.0, 100.0], 0.0), [2.0, 3.0])

    def test_tamanhos_diferentes_levanta_erro(self):
        with self.assertRaises(ValueError):
            dar_passo([1.0, 2.0], [1.0], 0.1)

    def test_nao_altera_as_entradas(self):
        w, ajuste = [1.0, 1.0], [10.0, -20.0]
        dar_passo(w, ajuste, 0.1)
        self.assertEqual(w, [1.0, 1.0])
        self.assertEqual(ajuste, [10.0, -20.0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
