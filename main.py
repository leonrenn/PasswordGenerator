"""
Short script to generate random but secure passwords.
"""

# MODULES
import random


# MAIN

def main() -> None:
    opt = "all"
    while True:
        try:
            number_of_characters = int(input("How many characters?"))
            break
        except TypeError:
            print("Provide a valid argument!\n")
    if opt == "all":
        characters = [chr(i) for i in range(33, 127)]  # beginning with !
    password = [random.choice(characters) for _ in range(number_of_characters)]
    print("".join(password))
    return


# START PROGRAM

if __name__ == "__main__":
    main()
