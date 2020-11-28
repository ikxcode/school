import hashlib
import unicodedata
import sys


def authenticate(password, password_checksum):
    normalised_password = unicodedata.normalize("NFKD", password).encode("ascii", "ignore")
    checksummifier = hashlib.md5()
    checksummifier.update(normalised_password)

    if password_checksum == checksummifier.hexdigest():
        print("Correct password \n")
    else:
        print("Invalid password")
        print("Exiting game...")
        sys.exit()


def prompt_for_password():
    player1_password_checksum = "2ca3b093eacd099fc8b7f9cfdefebec5"
    player2_password_checksum = "c1e853fcba4b2dd76c2940774700777f"

    player1_password = input("Player 1 password: ")
    authenticate(player1_password, player1_password_checksum)

    player2_password = input("Player 2 password: ")
    authenticate(player2_password, player2_password_checksum)
