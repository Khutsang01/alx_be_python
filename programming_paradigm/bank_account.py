# Simple Bank Account Class

class BankAccount:
    """
    A class to represent a bank account, encapsulating
    common banking operations like deposit, withdrawal, and balance display.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float): The starting balance for the account.
                                     Defaults to 0.0.
        """
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            print("Invalid initial balance. Setting to 0.")
            self.__account_balance = 0.0
        else:
            self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Invalid deposit amount. Must be a positive number.")
            return
        self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Invalid withdrawal amount. Must be a positive number.")
            return False
        
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current balance of the account in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")