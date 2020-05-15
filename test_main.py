import unittest
from main import Account, Client, Historic, CheckingAccount, SavingAccount


class TestMain(unittest.TestCase):

    def setUp(self):
        # Clients
        self.c_1 = Client("Ana", "Silva", "555.042.695-95")
        self.c_2 = Client("Pedro", "Ramos", "024.542.358-20")

        # "Normal" accounts
        self.a_1 = Account("1476-6", self.c_1, "5000")
        self.a_2 = Account("1356-7", self.c_2, "6000")

        # Saving accounts
        self.sa_1 = SavingAccount("3574-6", self.c_1, "2000")
        self.sa_2 = SavingAccount("4751-3", self.c_2, "3000")

        # Checking accounts
        self.ca_1 = CheckingAccount("3687-1", self.c_1, "4000")
        self.ca_2 = CheckingAccount("1473-5", self.c_2, "1000")

    def tearDown(self):
        pass

    def test_first(self):
        self.assertEqual(self.c_1.first, "Ana")
        self.assertEqual(self.c_2.first, "Pedro")

    def test_account_number(self):
        self.assertIsNot(self.a_1._number, "1111-1")
        self.assertIsNot(self.a_2._number, "2222-2")

    def test_cpf(self):
        self.assertIsNot(self.c_1.cpf, "000.000.000-00")
        self.assertIsNot(self.c_2.cpf, "111.111.111-11")

    def test_deposit(self):
        self.a_1.deposit(50)
        self.a_2.deposit(60)

        self.assertEqual(self.a_1.bank_statement(), 5050.0)
        self.assertEqual(self.a_2.bank_statement(), 6060.0)

    def test_transfer_to(self):
        self.a_1.transfer_to(self.a_2, 500)

        self.assertEqual(self.a_1.bank_statement(), 4500.0)
        self.assertEqual(self.a_2.bank_statement(), 6500.0)

    def test_saving_account(self):
        self.sa_1.update(0.01)
        self.sa_2.update(0.02)

        self.assertEqual(self.sa_1._balance, 2060)
        self.assertEqual(self.sa_2._balance, 3180)

    def test_checking_account(self):
        pass


if __name__ == "__main__":
    unittest.main()
