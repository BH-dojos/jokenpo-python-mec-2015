import unittest
from main import Rodada

class TestDojo(unittest.TestCase):

    def setUp(self):
        pass

    def test_pedra_perde_do_papel(self):
        rodada = Rodada("Pedra", "Papel")
        self.assertEqual("Papel", rodada.vencedor())

    def test_papel_ganha_da_pedra(self):
        rodada = Rodada("Papel", "Pedra")
        self.assertEqual("Papel", rodada.vencedor())

    def test_pedra_ganha_de_tesoura(self):
        rodada = Rodada("Pedra", "Tesoura")
        self.assertEqual("Pedra", rodada.vencedor())

    def test_tesoura_perde_de_pedra(self):
        rodada = Rodada("Tesoura", "Pedra")
        self.assertEqual("Pedra", rodada.vencedor())

    def test_tesoura_ganha_de_papel(self):
        rodada = Rodada("Tesoura", "Papel")
        self.assertEqual("Tesoura", rodada.vencedor())

    def test_papel_perde_de_tesoura(self):
        rodada = Rodada("Papel", "Tesoura")
        self.assertEqual("Tesoura", rodada.vencedor())


if __name__ == '__main__':
    unittest.main()