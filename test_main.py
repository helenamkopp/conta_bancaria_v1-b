import unittest
from main import Account, Client, Historic


class TestMain(unittest.TestCase):

    def setUp(self):
        self.c_1 = Client("Ana", "Silva", "555.042.695-95")
        self.c_2 = Client("Pedro", "Ramos", "024.542.358-20")

        self.a_1 = Account("1476-6", self.c_1, "5000")
        self.a_2 = Account("1356-7", self.c_2, "6000")

    def tearDown(self):
        pass

    def test_first(self):
        self.assertEqual(self.c_1.first, "Ana")
        self.assertEqual(self.c_2.first, "Pedro")

    def test_account_number(self):
        self.assertIsNot(self.a_1.number, "1111-1")
        self.assertIsNot(self.a_2.number, "2222-2")

    def test_cpf(self):
        self.assertIsNot(self.c_1.cpf, "000.000.000-00")
        self.assertIsNot(self.c_2.cpf, "111.111.111-11")

    def test_deposit(self):
        self.a_1.deposit(50)
        self.a_2.deposit(60)

        self.assertEqual(self.a_1.bank_statement(), 5050.0)
        self.assertEqual(self.a_2.bank_statement(), 6060.0)


if __name__ == "__main__":
    unittest.main()
