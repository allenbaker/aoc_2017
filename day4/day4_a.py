with open("input.txt", "r") as file:

    amount_of_valid_passphrases = 0
    for line in file:
        passphrase = line.split()
        unique_phrases = set(passphrase)
        if len(passphrase) == len(unique_phrases):
            amount_of_valid_passphrases += 1
    print(amount_of_valid_passphrases)
