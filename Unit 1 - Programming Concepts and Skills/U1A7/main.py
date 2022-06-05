import bank_account
import random
import numpy as np

acc = bank_account.BankAccount("William", 1356, "777 Myintzu Street", 2000)
acc.withdraw(3000)
acc.deposit(8000)
acc.withdraw(4000)
acc.show_profile()


def make_random_sorted_array(arr_len: int) -> list:
    arr = list()
    for i in range(arr_len):
        arr.append(random.randint(0, 99))

    np.sort(arr)
    print(arr)


make_random_sorted_array(20)
