# Class 1: Stores private/confidential data and exposes safe methods
class MobileMoneyAccount:
    """
    Manages a single mobile money account, using encapsulation to protect
    the balance and PIN.
    """
    # Class-level constant for the maximum transaction limit rule
    MAX_DAILY_TRANSACTION = 70000

    def __init__(self, account_holder, initial_balance=0.0):
        # Private attributes are conventionally prefixed with a double underscore
        self.__account_holder = account_holder
        self.__balance = initial_balance
        self.__pin = "1234"  # Default/Example PIN (In reality, this would be hashed)
        self.__daily_withdrawn_today = 0.0 # Track for the district-specific rule

    # --- Safe Methods to Update/Mutate Data ---

    def deposit(self, amount):
        """Adds funds to the account."""
        if amount > 0:
            self.__balance += amount
            return True, f"Deposit of {amount:,.2f} successful. New balance: {self.__balance:,.2f}"
        return False, "Deposit amount must be positive."

    def withdraw(self, amount, pin_attempt):
        """
        Withdraws funds, enforcing PIN check, balance check, and the daily limit rule.
        This is the method that enforces the district-specific numeric rule.
        """
        if pin_attempt != self.__pin:
            return False, "Withdrawal failed: Invalid PIN."

        if amount <= 0:
            return False, "Withdrawal amount must be positive."

        # Enforce the district-specific numeric rule: Max Daily Transaction Limit
        if self.__daily_withdrawn_today + amount > self.MAX_DAILY_TRANSACTION:
            remaining_limit = self.MAX_DAILY_TRANSACTION - self.__daily_withdrawn_today
            return False, f"Withdrawal failed: Exceeds daily limit of {self.MAX_DAILY_TRANSACTION:,.2f}. Remaining limit: {remaining_limit:,.2f}"

        if amount <= self.__balance:
            self.__balance -= amount
            self.__daily_withdrawn_today += amount
            return True, f"Withdrawal of {amount:,.2f} successful. New balance: {self.__balance:,.2f}"
        else:
            return False, "Withdrawal failed: Insufficient balance."

    # --- Safe Methods to View Data ---

    def check_balance(self, pin_attempt):
        """Provides the current balance after a PIN check."""
        if pin_attempt == self.__pin:
            return True, f"Current balance for {self.__account_holder}: {self.__balance:,.2f}"
        return False, "Balance check failed: Invalid PIN."

    def get_account_holder(self):
        """A simple public getter for non-sensitive data."""
        return self.__account_holder

    def get_daily_withdrawn(self):
        """Exposes the internal tracker for the rule."""
        return self.__daily_withdrawn_today


# Class 2: Interacts with Class 1 externally without breaking encapsulation
class SimpleTransactionService:
    """
    Simpler service that interacts with the account methods directly
    and only returns the result.
    """
    def __init__(self, account):
        # Assumes the account object has been passed in
        self.account = account

    def process_withdrawal(self, amount, pin):
        """Delegates withdrawal to the account and returns the result."""
        # The primary function is to call the account's method
        return self.account.withdraw(amount, pin)

    def process_deposit(self, amount):
        """Delegates deposit to the account and returns the result."""
        # The primary function is to call the account's method
        return self.account.deposit(amount)

    def check_account_status(self, pin):
        """Delegates balance check to the account and returns the result."""
        # The primary function is to call the account's method
        return self.account.check_balance(pin)

# --- How this is simpler ---
# 1. Removed all print() statements. The calling code (outside this class)
#    is now responsible for displaying the status and message.
# 2. Removed the printing of the account holder's name for every transaction.
# 3. Removed the printing of the "Total withdrawn today" figure.
# 4. The methods are now concise wrappers that simply return the results
#    from the underlying account methods.

# 1. Setup the Mobile Money System
user_account = MobileMoneyAccount(account_holder="Alice", initial_balance=75000.00)
agent_service = SimpleTransactionService(user_account)

print(f"Initial Setup: Account Holder is {user_account.get_account_holder()}")
print(f"District Numeric Rule: Max Daily Withdrawal is {MobileMoneyAccount.MAX_DAILY_TRANSACTION:,.2f}")


# 2. Successful Deposit and Withdrawal
agent_service.process_deposit(5000)
agent_service.process_withdrawal(20000, "1234") # First withdrawal
user_account.check_balance("1234")


# 3. Demonstration of PIN/Security Encapsulation
agent_service.process_withdrawal(1000, "0000") # Wrong PIN attempt


# 4. Demonstration of the Numeric Rule (Max Daily Transaction Limit)
# Alice has already withdrawn 20,000. Limit remaining is 70,000 - 20,000 = 50,000

# This withdrawal is exactly the remaining limit (50,000) - Should SUCCEED
agent_service.process_withdrawal(50000, "1234")

# This withdrawal BREAKS the rule (Total will be 20,000 + 50,000 + 1,000 = 71,000) - Should FAIL
agent_service.process_withdrawal(1000, "1234")


# 5. Demonstration: Design Prevents Direct Modification (The Power of Encapsulation)
print("\n--- Demonstration of Direct Modification Prevention ---")

# A developer/hacker might try to modify the balance directly (e.g., to give themselves 1 Million)
print(f"Balance BEFORE direct access attempt: {user_account.check_balance('1234')[1]}")

try:
    # Attempt to directly modify the private attribute __balance
    user_account.__balance = 1000000.00
    print("WARNING: Direct modification seemed to work (though it didn't change the actual balance)")
except AttributeError as e:
    # In a truly strict language, this would be a hard error.
    # In Python, this creates a new *public* attribute called __balance that is separate from the *private* one.
    print(f"Direct access attempt failed (AttributeError would occur in a subclass scenario): {e}")

# This shows that the internal private data is UNCHANGED
print(f"Balance AFTER direct access attempt: {user_account.check_balance('1234')[1]}")

# If we try to access the "private" internal balance, Python changes the name to _MobileMoneyAccount__balance
try:
    print(f"Direct access using name mangling (A hack, not breaking encapsulation's intent): {user_account._MobileMoneyAccount__balance:,.2f}")
    # Even this "hack" is discouraged, but shows the true internal value is only changed by safe methods.
    user_account._MobileMoneyAccount__balance = 1000000.00
    print("SUCCESS: A hacker bypassed protection using name-mangling, showing Python's soft encapsulation.")
except AttributeError:
    print("FAIL: The internal data is truly protected.")

print(f"Final Balance after all attempts: {user_account.check_balance('1234')[1]}")        