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

    def test_deposit(self):
        self.a_1.deposit(50)
        self.a_2.deposit(60)

        self.assertEqual(self.a_1.bank_statement(), 5050.0)
        self.assertEqual(self.a_2.bank_statement(), 6060.0)


if __name__ == "__main__":
    unittest.main()