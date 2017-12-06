with open("input.txt", "r") as file:

    def is_passphrase_valid(passphrase):
        for i, item in enumerate(passphrase):
            for j in range(i + 1, len(passphrase)):
                if len(item) == len(passphrase[j]) and sorted(item) == sorted(passphrase[j]):
                    return False
        return True

    amount_of_valid_passphrases = 0
    for line in file:
        raw_values = line.split()
        if is_passphrase_valid(raw_values):
            amount_of_valid_passphrases += 1

    print(amount_of_valid_passphrases)






