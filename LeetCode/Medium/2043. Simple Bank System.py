from threading import Lock

class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.accNum = len(balance)
        self.balance = balance
        self._lock = Lock()
    
    def checkNum(self, acc):
        return 1 <= acc <= len(self.balance)
        

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if self.checkNum(account1) and self.checkNum(account2):
            if self.withdraw(account1, money):
                self.deposit(account2, money)
                return True
        return False
        

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        with self._lock:
            if self.checkNum(account):
                self.balance[account-1] += money
                return True
            return False

        

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        idx = account - 1
        with self._lock:
            if self.checkNum(account):
                if self.balance[idx] >= money:
                    self.balance[idx] -= money
                    return True
            return False 
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
