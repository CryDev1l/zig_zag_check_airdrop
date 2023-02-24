with open("addresses.txt", "r") as f:
    addresses_list = [row.strip() for row in f]
with open("wallets.txt", "r") as f:
    wallets_list = [row.strip() for row in f]
for wallet in wallets_list:
    wallet = wallet.lower()
    if wallet in addresses_list:
        print(f'{wallet} Имеет право на дроп')
    else:
        print(f'{wallet} Не имеет право на дроп')
