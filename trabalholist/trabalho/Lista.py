import unittest

# Para realizar os testes, Deve se usar uma biblioteca de testes como o unittestou o pytest.
# Exercício 1


def soma(a, b):
    return a + b


class TestSoma(unittest.TestCase):
    def test_soma_positiva(self):
        self.assertEqual(soma(3, 5), 8)

    def test_soma_negativa(self):
        self.assertEqual(soma(-2, -3), -5)

    def test_soma_mista(self):
        self.assertEqual(soma(4, -7), -3)

# Exercício 2


def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)


class TestFatorial(unittest.TestCase):
    def test_fatorial_zero(self):
        self.assertEqual(fatorial(0), 1)

    def test_fatorial_positivo(self):
        self.assertEqual(fatorial(5), 120)

# Exercício 3


class Calculadora:
    def adicao(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b


class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_adicao(self):
        self.assertEqual(self.calc.adicao(3, 5), 8)

    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(8, 4), 4)

    def test_multiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(2, 6), 12)

    def test_divisao(self):
        self.assertEqual(self.calc.divisao(10, 2), 5)
        self.assertRaises(ValueError, self.calc.divisao, 5, 0)

# Exercício 4


def eh_par(numero):
    return numero % 2 == 0


class TestEhPar(unittest.TestCase):
    def test_par(self):
        self.assertTrue(eh_par(4))

    def test_impar(self):
        self.assertFalse(eh_par(7))

# Exercício 5


class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def deposito(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor

    def saque(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor


class TestContaBancaria(unittest.TestCase):
    def setUp(self):
        self.conta = ContaBancaria(100)

    def test_deposito(self):
        self.conta.deposito(50)
        self.assertEqual(self.conta.saldo, 150)

    def test_saque(self):
        self.conta.saque(30)
        self.assertEqual(self.conta.saldo, 70)

    def test_saque_saldo_insuficiente(self):
        self.assertRaises(ValueError, self.conta.saque, 120)

# Exercício 6


def contar_vogais(string):
    vogais = "aeiouAEIOU"
    return len([char for char in string if char in vogais])


class TestContarVogais(unittest.TestCase):
    def test_contar_vogais(self):
        self.assertEqual(contar_vogais("Hello World"), 3)

    def test_sem_vogais(self):
        self.assertEqual(contar_vogais("Brrr"), 0)

# Exercício 7


def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


class TestEhPrimo(unittest.TestCase):
    def test_primo(self):
        self.assertTrue(eh_primo(7))

    def test_nao_primo(self):
        self.assertFalse(eh_primo(10))

# Exercício 8


def ordenar_lista(lista):
    return sorted(lista)


class TestOrdenarLista(unittest.TestCase):
    def test_ordenar_lista(self):
        self.assertEqual(ordenar_lista([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [
                         1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

# Exercício 9


def calcular_media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)


class TestCalcularMedia(unittest.TestCase):
    def test_media(self):
        self.assertEqual(calcular_media([2, 4, 6, 8]), 5.0)

    def test_lista_vazia(self):
        self.assertEqual(calcular_media([]), 0)

# Exercício 10


def inverter_string(string):
    return string[::-1]


class TestInverterString(unittest.TestCase):
    def test_inverter_string(self):
        self.assertEqual(inverter_string("Hello"), "olleH")

    def test_inverter_string_vazia(self):
        self.assertEqual(inverter_string(""), "")

# Exercício 11


def somar_lista(lista):
    soma = 0
    for numero in lista:
        if isinstance(numero, (int, float)):
            soma += numero
    return soma


class TestSomarLista(unittest.TestCase):
    def test_somar_lista(self):
        self.assertEqual(somar_lista([1, 2, 3, -4, 5.5]), 7.5)

    def test_lista_vazia(self):
        self.assertEqual(somar_lista([]), 0)


if __name__ == '__main__':
    unittest.main()
