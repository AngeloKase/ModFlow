import unittest


def validar_nome(nome):
    return len(nome.strip()) > 0


class TestValidacao(unittest.TestCase):

    def test_nome_valido(self):
        self.assertTrue(validar_nome("Trabalho"))

    def test_nome_vazio(self):
        self.assertFalse(validar_nome(""))

    def test_nome_espaco(self):
        self.assertFalse(validar_nome("    "))


if __name__ == "__main__":
    unittest.main()
