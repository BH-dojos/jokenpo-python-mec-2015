import unittest
from main import Rodada

class TestDojo(unittest.TestCase):

    def setUp(self):
        pass

    def test_pedra_perde_do_papel(self):
        rodada = Rodada("Pedra", "Papel")
        assert rodada.vencedor() == "Papel"

if __name__ == '__main__':
    unittest.main()