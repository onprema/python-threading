# Example of a race condition
from training import Account
from concurrent.futures import ThreadPoolExecutor


if __name__ == '__main__':
    print('Main thread starting')
    account = Account()
    print(account)
    with ThreadPoolExecutor(max_workers=2) as executor:
        # Submit two threads: deposit 100, followed by withdrawal 50
        for transaction, amount in [(account.deposit, 100), (account.withdrawal, 50)]:
            executor.submit(transaction, amount)
    print(account)
    print('Main thread ending')

