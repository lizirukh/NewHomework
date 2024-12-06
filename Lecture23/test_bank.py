import unittest
import bank

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        print("SetUp")
        self.bankAccount = bank.BankAccount("John Doe", 5000)

    def tearDown(self):
        print('TearDown')

    def test_deposit(self):
        self.bankAccount.deposit(1000)
        self.assertEqual(self.bankAccount.balance, 6000)

        with self.assertRaises(ValueError) as context:
            self.bankAccount.deposit(0)

        with self.assertRaises(ValueError) as context:
            self.bankAccount.deposit(-1)

        self.assertEqual(str(context.exception), "Deposit amount must be positive")


    def test_withdraw(self):
        self.bankAccount.withdraw(1000)
        self.assertEqual(self.bankAccount.balance, 4000)

        with self.assertRaises(ValueError) as context:
            self.bankAccount.withdraw(5001)

        self.assertEqual(str(context.exception), "Insufficient funds")

    def test_get_balance(self):
        self.assertEqual(self.bankAccount.get_balance(), 5000)
